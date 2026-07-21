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

# funcion para calcular el dinero enviado y recibido 
def calculate_send_recipient_money(user_id:str):

    db = get_db()

    cursor = db.execute(
        "SELECT id, acount_number FROM acounts WHERE user_id = ?", (user_id, ), 
    )

    acount = cursor.fetchone()
    acount_id = acount['id']
    acount_number = acount['acount_number']

    # al usar fetchall se van a guardar todas las filas que cumplan las condiciones de la query
    # estas filas se pueden interpretar como objetos {"key":"value"}
    rows = db.execute (
        '''
            SELECT
                t.amount,
                sender.acount_number AS sender_acount_number,
                recipient.acount_number AS recipient_acount_number
            FROM transactions AS t
            JOIN acounts AS sender
                ON t.sender_acount_id = sender.id
            JOIN acounts AS recipient
                ON t.recipient_acount_id = recipient.id
            WHERE t.sender_acount_id = ? OR t.recipient_acount_id = ?
            ORDER BY t.created_at DESC
        ''',
        (acount_id, acount_id, ),
    ).fetchall()

    # podemos crear una lista de diccionario para los filas de tipo row de rows
    data = []

    # cada row es una fila de rows, donde cada fila de rows se puede iterar como un objeto o diccionario con clave-valor
    # {'created_at': date}

    for row in rows:
        data.append({
            'amount' : row['amount'],
            'sender_acount_number' : row['sender_acount_number'],
            'recipient_acount_number' : row['recipient_acount_number']
        })
    
    send_money = 0
    recipient_money = 0

    for d in data:

        if d['sender_acount_number'] == acount_number:
            send_money += d['amount']
        
        if d['recipient_acount_number'] == acount_number:
            recipient_money += d['amount']
    
    return send_money, recipient_money