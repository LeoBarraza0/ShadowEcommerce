from flask import Blueprint, render_template, session, jsonify, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/productos')
def productos():
    return render_template('productos.html')

@main.route('/sobre_nosotros')
def sobre_nosotros():
    return render_template('sobre_nosotros.html')

@main.route('/contacto')
def contacto():
    return render_template('contacto.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/registroUsuario')
def registro_usuario():
    return render_template('registroUsuario.html')

@main.route('/carrito')
def carrito():
    return render_template('carrito.html')

@main.route('/panel_admin')
def panel_admin():
    return render_template('panel_admin.html')


@main.route('/adminprod')
def adminprod():
    return render_template('adminprod.html')

@main.route('/adminusers')
def adminusers():
    return render_template('adminusers.html')
