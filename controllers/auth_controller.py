from flask import Blueprint, request, jsonify, session, url_for
from models.__init__ import db
from models.cliente import Cliente
from models.admin import Admin  # Importar el modelo Admin
from werkzeug.security import generate_password_hash, check_password_hash

auth_controller = Blueprint('auth_controller', __name__)

@auth_controller.route('/registro', methods=['POST'])
def registrar_usuario():
    datos = request.json
    print(f"Datos recibidos para registro: {datos}")  # Mensaje de depuración
    id_cliente = datos.get('id_cliente')
    nombre = datos.get('nombre')
    direccion = datos.get('direccion')
    correo = datos.get('correo')
    password = generate_password_hash(datos.get('password'), method='pbkdf2:sha256')
    nuevo_cliente = Cliente(id_cliente=id_cliente, nombre=nombre, direccion=direccion, correo=correo, password=password)

    try:
        db.session.add(nuevo_cliente)
        db.session.commit()
        return jsonify({'mensaje': 'Usuario registrado exitosamente'}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'mensaje': 'Error al registrar el usuario'}), 500

@auth_controller.route('/login', methods=['POST'])
def login_post():
    datos = request.json
    print(f"Datos recibidos para login: {datos}")  # Mensaje de depuración
    correo = datos.get('correo')
    print(correo)
    contraseña = datos.get('contraseña')
    print(contraseña)
    # Verificar si el correo pertenece a un cliente
    cliente = Cliente.query.filter_by(correo=correo).first()
    if cliente and check_password_hash(cliente.password, contraseña):
        session['user_id'] = cliente.id_cliente
        session['nombre'] = cliente.nombre
        session['correo'] = cliente.correo
        session['direccion'] = cliente.direccion
        return jsonify({'success': True, 'redirect': url_for('main.index')})

    # Verificar si el correo pertenece a un administrador
    admin = Admin.query.filter_by(correo=correo).first()
    if admin and (admin.password == contraseña):
        session['user_id'] = admin.id
        session['nombre'] = admin.nombre
        session['correo'] = admin.correo
        session['direccion'] = ''
        return jsonify({'success': True, 'redirect': url_for('main.panel_admin')})
    else:
        print("No encontrado")

    # Si no se encuentra el usuario en ninguna tabla
    return jsonify({'success': False, 'mensaje': 'Correo o contraseña incorrectos'}), 400