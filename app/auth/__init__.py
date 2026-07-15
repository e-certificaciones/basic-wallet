from flask import Blueprint

auth_bp = Blueprint(
    "auth", # identificador interno (nombre del Blueprint)
    __name__, # ubicacion del modulo actual
    url_prefix="/auth" # prefijo para todas las url del Blueprint
)

from app.auth import routes # registra las rutas al importar