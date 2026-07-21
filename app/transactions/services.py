from decimal import Decimal # representa cantidades monetarias de forma exacta
import re, random

REG_EXP_ACOUNT_NUMBER = r"^[0-9]{12}$"

# validar el numero de cuenta con expresion regular
def validate_acount_number(acount_number:str):

    if re.fullmatch(REG_EXP_ACOUNT_NUMBER, acount_number):
        return True

    return False

# valida si el dato ingresado es de tipo numerico
def validate_amount(amount:str):

    try:
        amount_decimal = Decimal(amount)

        if amount_decimal > 0:
            return amount_decimal
        
        return False
    except:
        return False
    
# generador de numero de 12 digitos para los account numbers
def generate_transaction_number():

    n = random.randint(1, 999_999)

    return f"{n:06d}" # se le indica que formatee n, si n no cumple con 12 digitos rellena con 0 a la izquierda, la d indica decimal
