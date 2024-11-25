from flask import Flask
from models import db
from views.main import main as main_blueprint
from controllers.auth_controller import auth_controller as auth_blueprint
from controllers.transaccion_controller import transaccion_controller as transaccion_blueprint
from controllers.producto_controller import producto_controller as producto_blueprint
from controllers.contacto_controller import contacto_controller as contacto_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/shadows'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'tu_clave_secreta_aqui'

db.init_app(app)

def register_blueprints(app):
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(transaccion_blueprint)
    app.register_blueprint(producto_blueprint)
    app.register_blueprint(contacto_blueprint)

register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)