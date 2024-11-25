from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transaccion(db.Model):
    id_transaccion = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Float, nullable=False)
    direccion_envio = db.Column(db.String(200), nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    detalles = db.relationship('DetalleTrans', backref='transaccion', lazy=True)

class DetalleTrans(db.Model):
    id_detalle = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    id_transaccion_fk = db.Column(db.Integer, db.ForeignKey('transaccion.id_transaccion'), nullable=False)
    bruto = db.Column(db.Float, nullable=False)
    neto = db.Column(db.Float, nullable=False)
    id_producto = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    imp = db.Column(db.Float, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)