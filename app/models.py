from app import db

class Equipos(db.Model):
    equipo_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    direccionIPV4 = db.Column(db.String(15), nullable=False)
    isOnline = db.Column(db.Boolean)

    def __init__(self, nombre, direccionIPV4, isOnline):
        self.nombre = nombre
        self.direccionIPV4 = direccionIPV4
        self.isOnline = isOnline
