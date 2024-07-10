# Importar las bibliotecas necesarias
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import hashlib

# Configuración básica de la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'  # Conexión a la base de datos SQLite
db = SQLAlchemy(app)

# Modelo de la tabla de usuarios
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    hash_password = db.Column(db.String(120), nullable=False)

# Rutas y funciones de la aplicación Flask
@app.route('/registro', methods=['POST'])
def registrar_usuario():
    datos = request.get_json()
    nombre = datos['nombre']
    password = datos['password']
    hash_password = hashlib.sha256(password.encode()).hexdigest()

    nuevo_usuario = Usuario(nombre=nombre, hash_password=hash_password)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'mensaje': 'Usuario registrado correctamente'})

@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    nombre = datos['nombre']
    password = datos['password']
    hash_password = hashlib.sha256(password.encode()).hexdigest()

    usuario = Usuario.query.filter_by(nombre=nombre, hash_password=hash_password).first()
    if usuario:
        return jsonify({'mensaje': 'Inicio de sesión exitoso'})
    else:
        return jsonify({'error': 'Nombre de usuario o contraseña incorrectos'})

# Crear la base de datos SQLite antes de ejecutar la aplicación Flask
with app.app_context():
    db.create_all()

# Iniciar la aplicación Flask en el puerto 5800
if __name__ == '__main__':
    app.run(port=5800, debug=True)
