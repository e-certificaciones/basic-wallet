from app.db import get_db

# retorna un diccionario de datos 
def index_information(user_id:str):

    db = get_db()

    cursor = db.execute(
        ''' SELECT name, last_name, acount_number, balance FROM users 
            JOIN acounts ON users.id = acounts.user_id WHERE users.id = ? ''',
        (user_id, ),
    )

    user_data = cursor.fetchone() # fetchone retorna un tipo row que crea una tupla con key y valores, user_data['name'] = name_bd
    # print(tuple(user_data))

    data = {}
    # usamos la tupla para crear un diccionario 
    for key in user_data.keys():
        data[key] = user_data[key]
    
    return data