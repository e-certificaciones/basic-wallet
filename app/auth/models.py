from app.db import get_db

def get_user_by_username(username):
    db = get_db()
    return db.execute(
        "SELECT * FROM users WHERE username = ?",
        (username, ), 
    )
    # la api de sqlite3 exige que se le pase una tupla como parametros (username, ), 