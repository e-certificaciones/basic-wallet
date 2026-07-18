from app.db import get_db
from app.auth.services import generate_account_number
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# si ya hay usuario con el mismo email y mismo usaername 
# retorna mensajes de error, si no , retorna un True
def validate_username_email(username:str, email:str):
    
    error = {}
    db = get_db()

    cursor = db.execute(
        "SELECT COUNT(*) AS total FROM users WHERE username = ?",
        (username, ),  # la api de sqlite3 exige que se le pase una tupla como parametros (username, ),
    )

    rows = cursor.fetchone() # convertir el cursor que retorna sqlite3 a una tupla
    rows = rows['total'] # acceder al valor retornado mediante el alias que usamos para COUNT(*)

    if rows != 0:
        error['username'] = "A user with that username already exists."

    cursor = db.execute(
        "SELECT COUNT(*) AS total FROM users WHERE email = ?",
        (email, ),
    )

    rows = cursor.fetchone()
    rows = rows['total']

    if rows != 0:
        error['email'] = "A user with that email already exists."

    if error:
        return error
    
    return True


def insert_user(name:str, last_name:str, username:str, email:str, password_hash:str, birthday:str):

    db = get_db()
    password_hash = generate_password_hash(password_hash)

    while True:

        try:
            # guardamos el valor de db.execute en un cursor para luego obtener el id de la ultima fila ingresada
            cursor = db.execute(
                "INSERT INTO users (username, password_hash, email, name, last_name, birthday) VALUES(?,?,?,?,?,?)",
                (username, password_hash, email, name, last_name, birthday, ),
            )

            # cuando no necesitemos usar lastrowid no hay necesidad de guardar la ejecucion de in insert en un cursor 
            user_id = cursor.lastrowid
        
            n = generate_account_number()

            db.execute(
                "INSERT INTO acounts(user_id, account_number, balance) VALUES(?,?,?)",
                (user_id, n, 10000, ),
            )

            db.commit() # si ocurre un error no llega a ejecutarse el break
            break
        except sqlite3.IntegrityError as e: # el integrity error es cuando se violenta el unique de un campo en este caso intentar guardar el mimo acont numer
            db.rollback() # hace un rollback de las operaciones antes del commit de la instacia de la bd

# si el usuario y contrase;ia coinciden retornar True, si no False
def validate_username_and_password(username:str, password:str):

    db = get_db()

    cursor = db.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        (username, ),
    )

    password_db = cursor.fetchone()

    if password_db is not None: # si la consulta esta vacia el execute retorna un None

        password_db = password_db['password_hash']
   
        if check_password_hash(password_db, password):
            return True
    
    return False

# retorna el id de un usuario tomando como parametro su username
def user_id_by_username(username:str):

    db = get_db()

    cursor = db.execute(
        "SELECT id FROM users WHERE username = ?",
        (username, ), 
    )

    user_id = cursor.fetchone()
    user_id = user_id['id']

    return user_id
    
