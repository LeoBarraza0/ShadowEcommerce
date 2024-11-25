from flask import Blueprint, request, jsonify, session
from models.contacto import Contacto, db

contacto_controller = Blueprint('contacto_controller', __name__)

@contacto_controller.route('/insertar_contacto', methods=['POST'])
def insertar_contacto():
    data = request.get_json()
    nombre = data.get('nombre')
    correo = data.get('correo')
    telefono = data.get('telefono')
    mensaje = data.get('mensaje')
    id_cliente_fk = session['user_id']

    nuevo_contacto = Contacto(
        id_cliente_fk=id_cliente_fk,
        nombre=nombre,
        correo=correo,
        telefono=telefono,
        mensaje=mensaje
    )

    try:
        db.session.add(nuevo_contacto)
        db.session.commit()
        return jsonify({'success': True, 'mensaje': 'Mensaje enviado correctamente'}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'mensaje': 'Error al insertar los datos en la base de datos'}), 500