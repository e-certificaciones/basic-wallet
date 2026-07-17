from flask import Flask, render_template
from app.config import Config
from app.extensions import sess
from app.auth import auth_bp
from app.db import close_db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # el objeto sess que  creamos en extensions.py lo usamos oara configurar el sistema de sesiones
    # las inicializamos en esta aplicacion, init_app, solo debe haber un objeto de sesion por aplicacion
    # tambien lee los atributos de la clase Config
    sess.init_app(app)

    # cierra las conexiones a la bd cada vez que le indicamos al navegador cambiar de url (request)
    app.teardown_appcontext(close_db)
    
    # Blueprints
    app.register_blueprint(auth_bp)

    @app.route("/ping")
    def ping():
        return render_template("layout.html", string="HI")

    return app
