from app.db import get_db
from flask import session
from app.transactions.services import validate_acount_number, validate_amount

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


