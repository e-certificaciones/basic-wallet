from flask import Blueprint

acounts_bp = Blueprint(
    "acounts",
    __name__,
    url_prefix="/acounts"
)

from app.acounts import routes