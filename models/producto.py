from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Producto(db.Model):
    id_producto = db.Column(db.String(100), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    img = db.Column(db.String(200))
    precio = db.Column(db.Float, nullable=False)