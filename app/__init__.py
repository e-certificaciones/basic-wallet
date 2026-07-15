from flask import Flask
from app.config import Config
from app.extensions import sess
from app.auth import auth_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # el objeto sess que  creamos en extensions.py lo usamos oara configurar el sistema de sesiones
    # las inicializamos en esta aplicacion, init_app, solo debe haber un objeto de sesion por aplicacion
    # tambien lee los atributos de la clase Config
    sess.init_app(app)

    # Blueprints
    app.register_blueprint(auth_bp)

    @app.route("/ping")
    def ping():
        return "ok"

    return app
