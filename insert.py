from app import app, db  # Importa la instancia de app y db
from models.admin import Admin  # Asegúrate de tener un modelo Admin definido
from werkzeug.security import generate_password_hash

# Establece el contexto de la aplicación
with app.app_context():
    # Crea un nuevo administrador
    nuevo_admin = Admin(
        nombre="Admin Principal",
        correo="admin1@ejemplo.com",
        password='123'
    )
    db.session.add(nuevo_admin)
    db.session.commit()

    print("Administrador creado con éxito")