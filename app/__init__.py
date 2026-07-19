from flask import Flask, render_template, session, redirect, url_for
from app.config import Config
from app.extensions import sess
from app.auth import auth_bp
from app.db import close_db
from app.acounts import acounts_bp
from app.helpers import usd
from app.transactions import transactions_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # el objeto sess que  creamos en extensions.py lo usamos oara configurar el sistema de sesiones
    # las inicializamos en esta aplicacion, init_app, solo debe haber un objeto de sesion por aplicacion
    # tambien lee los atributos de la clase Config
    sess.init_app(app) # despues de inicializar podemos crear sesiones en los archivos de routes, ademas de acceder a session

    # cierra las conexiones a la bd cada vez que le indicamos al navegador cambiar de url (request)
    app.teardown_appcontext(close_db)
    
    # filtro de jinja formatear cadenas de dinero en las plantillas
    app.jinja_env.filters["usd"] = usd

    # Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(acounts_bp)
    app.register_blueprint(transactions_bp)

    # es la ruta de apertura de la app
    @app.route("/")
    def index():
        if not session.get('user_id'):
            return redirect(url_for('auth.login'))
        
        return redirect(url_for('acounts.index')) 
       
    
    return app
