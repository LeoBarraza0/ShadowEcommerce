from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contacto(db.Model):
    id_contacto = db.Column(db.Integer, primary_key=True)
    id_cliente_fk = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    mensaje = db.Column(db.Text, nullable=False)