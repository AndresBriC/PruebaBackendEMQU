from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Equipos
import subprocess # To ping the IPs

# Dummy user data (replace this with a real database)
users = {'username': 'password'}

@app.route('/')
def home():
    equipos =  Equipos.query.all()
    return render_template('index.html', equipos=equipos)

# You can define your login and logout routes here
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the provided username and password match
        if users.get(username) == password:
            equipos = Equipos.query.all()
            return render_template('dashboard.html', equipos=equipos)
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/logout')
def logout():
    # Implement logout logic here (if needed)
    return redirect(url_for('home'))

@app.route('/equipos')
def list_equipos():
    equipos = Equipos.query.all()
    return render_template('equipos.html', equipos=equipos)

@app.route('/add', methods=['GET', 'POST'])
def add_equipo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccionIPV4 = request.form['direccionIPV4']
        equipo = Equipos(nombre=nombre, direccionIPV4=direccionIPV4, isOnline=False)
        db.session.add(equipo)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_equipo(id):
    equipo = Equipos.query.get(id)
    if request.method == 'POST':
        equipo.nombre = request.form['nombre']
        equipo.direccionIPV4 = request.form['direccionIPV4']

        online = ping_equipo(equipo.direccionIPV4)
        equipo.isOnline = online

        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('edit.html', equipo=equipo)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_equipo(id):
    equipo = Equipos.query.get(id)
    db.session.delete(equipo)
    db.session.commit()
    equipos = Equipos.query.all()
    return redirect(url_for('dashboard'))

@app.route('/dashboard', methods=['GET'])
def dashboard():
    equipos = Equipos.query.all()

    online_count = Equipos.query.filter_by(isOnline=True).count()
    offline_count = Equipos.query.filter_by(isOnline=False).count()

    return render_template('dashboard.html', equipos=equipos, online_count=online_count, offline_count=offline_count)

@app.route('/ping_all_equipos', methods=['POST'])
def ping_all_equipos():
    equipos = Equipos.query.all()
    online_count = 0
    offline_count = 0

    for equipo in equipos:
        online = ping_equipo(equipo.direccionIPV4)
        equipo.isOnline = online

        if online:
            online_count += 1
        else:
            offline_count += 1

    db.session.commit()

    return redirect(url_for('dashboard'))

def ping_equipo(ip):
    try:
        # Run the ping command and capture the output
        subprocess.check_output(["ping", "-c", "1", ip])
        print(f"Successfully pinged {ip}")

        # Check if the ping was successful (return code 0) and contains "1 packets transmitted"
        return True
    except Exception as e:
        # Handle exceptions, e.g., if the ping command fails
        print(f"Error pinging {ip}: {str(e)}")
        return False