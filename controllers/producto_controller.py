from flask import Blueprint, request, jsonify
from models.producto import Producto, db

producto_controller = Blueprint('producto_controller', __name__)

@producto_controller.route('/insertar_productos', methods=['POST'])
def insertar_productos():
    data = request.get_json()
    productos = data.get('productos', [])

    if not productos:
        return jsonify({'success': False, 'mensaje': 'No se proporcionaron productos'}), 400

    try:
        for producto in productos:
            nuevo_producto = Producto(
                id_producto=producto['id'],
                nombre=producto['titulo'],
                descripcion=producto.get('descripcion'),
                img=producto['imagen'],
                precio=producto['precio']
            )
            db.session.add(nuevo_producto)
        db.session.commit()
        return jsonify({'success': True, 'mensaje': 'Productos insertados correctamente.'}), 200
    except Exception as e:
        print(f"Error en la base de datos: {e}")
        return jsonify({'success': False, 'mensaje': f'Error al insertar productos: {e}'}), 500