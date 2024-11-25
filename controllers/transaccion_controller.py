from flask import Blueprint, request, jsonify
from models.transaccion import Transaccion, DetalleTrans, db
from datetime import datetime

transaccion_controller = Blueprint('transaccion_controller', __name__)

@transaccion_controller.route('/guardar_transaccion', methods=['POST'])
def guardar_transaccion():
    data = request.json
    monto = data['monto']
    direccion_envio = data['direccion_envio']
    id_cliente = data['id_cliente']
    fecha = data['fecha']
    productos = data['productos']

    try:
        fecha = datetime.fromisoformat(fecha)
    except ValueError as e:
        return jsonify({'success': False, 'mensaje': 'Formato de fecha incorrecto'}), 400

    nueva_transaccion = Transaccion(monto=monto, direccion_envio=direccion_envio, id_cliente=id_cliente, fecha=fecha)

    try:
        db.session.add(nueva_transaccion)
        db.session.commit()

        for producto in productos:
            detalle = DetalleTrans(
                cantidad=producto['cantidad'],
                id_transaccion_fk=nueva_transaccion.id_transaccion,
                bruto=producto['bruto'],
                neto=producto['neto'],
                id_producto=producto['titulo'],
                precio=producto['precio'],
                imp=producto['imp'],
                nombre=producto['nombre']
            )
            db.session.add(detalle)
        db.session.commit()
        return jsonify({'success': True, 'mensaje': 'Transacción guardada exitosamente'}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'mensaje': 'Error al guardar la transacción'}), 500