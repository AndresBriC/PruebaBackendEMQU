# Keys
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

SQL_USERNAME = env_vars["SQL_USERNAME"]
SQL_PASSWORD = env_vars["SQL_PASSWORD"]
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{SQL_USERNAME}:{SQL_PASSWORD}@localhost/pruebaEMQU'
