import sqlite3
from flask import current_app, g # almacen temporal de un request, en este caso es el almacen temporal de la bd

def get_db():
    if "db" not in g: 
        g.db = sqlite3.connect(current_app.config["DATABASE"]) #obtenemos la ruta de la bd usando las configuraciones de la app
        g.db.row_factory = sqlite3.Row # cada linea de los datos retornados van a ser leidos por el nombre de la columna, no por el indice de una lista

    return g.db #devuelve la conexion para usarla en models

def close_db():
    db = g.pop("db", None)
    if db is not None:
        db.close()