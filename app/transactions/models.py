from app.db import get_db
from flask import session
from datetime import datetime
from app.transactions.services import validate_acount_number, validate_amount, generate_transaction_number


# validamos que el numero de cuanta para hacer el deposito sea diferente
def validate_diferent_acount_number(acount_number:str, session_id:str):

    db = get_db()

    if not validate_acount_number(acount_number):
        return False
    
    cursor = db.execute(
        "SELECT user_id FROM acounts WHERE acount_number = ?",
        (acount_number, ),
    )

    user_id = cursor.fetchone() # si no  hay datos retorna None
    
    if user_id is None: 
        return False

    user_id = user_id['user_id']

    if user_id != session_id:
        return True

    return False
    
# retornamos informacion de la cuenta a hacer el deposito
def recipient_information(acount_number:str):

    db = get_db()

    cursor = db.execute(
        "SELECT user_id FROM acounts WHERE acount_number = ?",
        (acount_number, ),
    )

    user_id = cursor.fetchone()
    user_id = user_id['user_id']

    cursor = db.execute(
        "SELECT name, last_name FROM users WHERE id = ?",
        (user_id, ),
    )

    row = cursor.fetchone()
    data = {}

    for key in row.keys():
        data[key] = row[key]

    return data

# vaidar si el usuario tiene suficientes fondos en su cuenta 
def validate_suficient_balance(amount:str, user_id:str):
    
    db = get_db()

    if validate_amount(amount) == False:
        return -1
    
    amount_to_send = validate_amount(amount)

    cursor = db.execute(
        "SELECT balance FROM acounts WHERE user_id = ?",
        (user_id, ),
    )

    balance = cursor.fetchone()
    balance = balance['balance']
    
    if balance >= amount_to_send:
        return 1
    
    return 0

# funcion para hacer la tranferencia de dinero entre la cuenta del sender y el reicipient
#
def transfer_money(acount_number, amount, sender_user_id):

    db = get_db()

    while True:

        try:
            cursor = db.execute(
                "SELECT id FROM acounts WHERE user_id = ?",
                (sender_user_id, ),
            )
            
            sender_acount_id = cursor.fetchone()
            sender_acount_id = sender_acount_id['id']
            
            cursor = db.execute(
                "SELECT id FROM acounts WHERE acount_number = ?",
                (acount_number, ),
            )

            recipient_acount_id = cursor.fetchone()
            recipient_acount_id = recipient_acount_id['id']

            transaction_number = generate_transaction_number()
            today = datetime.now()
            
            # insertar la transaccion en la bd
            db.execute(
                "INSERT INTO transactions (sender_acount_id, recipient_acount_id, transaction_number, amount, concept, created_at) VALUES (?,?,?,?,?,?)",
                (sender_acount_id, recipient_acount_id, transaction_number, amount, "Deposit", today, ),
            )

            #actualizar balance en la cuenta del sender
            db.execute(
                "UPDATE acounts SET balance = balance - ? WHERE user_id = ?", 
                (amount, sender_user_id, ),
            )

            # actualizar el balance en la cuenta del reicipient
            db.execute(
                "UPDATE acounts SET balance = balance + ? WHERE acount_number = ?",
                (amount, acount_number, ), 
            )
            
            db.commit()
            break
        except:
            db.rollback()
            
#
# funcion que retorna un diccionario con las informacion de transacciones
def see_transactions_history(user_id:str):

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
                t.created_at,
                t.transaction_number,
                t.amount,
                t.concept,
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
            'created_at' : row['created_at'],
            'transaction_number' : row['transaction_number'],
            'amount' : row['amount'],
            'sender_acount_number' : row['sender_acount_number'],
            'recipient_acount_number' : row['recipient_acount_number']
        })
    
    return acount_number, data
