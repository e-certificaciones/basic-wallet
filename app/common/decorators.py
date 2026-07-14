from functools import wraps
from flask import session, redirect, url_for

# el parametro f es la funcion de cada ruta donde ocuparemos el decorador
# @login_required
def login_required(f):
    """
        wraps conserva la informacion de la funcion original como el nombre
        y documentacion, pero crea una una funcion temporal decorated_function

        usamos *args y **kwargs por si la funcion tiene argumentos en su ruta 
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # se usa session.get() porque no hay necesidad de que el usuario este logeado
        # no hay necesidad de usar session["user_id"]
        if session.get("user_id") is None:
            return redirect(url_for("auth.login"))

        return f(*args, **kwargs)
    return decorated_function