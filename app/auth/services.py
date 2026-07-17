"""
    este archivo contiene la logica, como validaciones
    y funcionalidad del modulo
"""
import re # para acceder a funciones de regular expresions
import random

REG_EXP_NAME = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$"  # la validacion para nombre y lastname es la misma
REG_EXP_EMAIL = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{3,}$"
REG_EXP_USERNAME = r"^[a-zA-Z0-9_áéíóúÁÉÍÓÚñÑ.-]+$"
REG_EXP_PASSWORD = r"^[a-zA-Z0-9._-]{6,}$"

# value es la cadena a validar, validation_type el tipo de validacion a aplicar 
def validate_input(value:str, validation_type:str):

    if validation_type == "name" or validation_type == "lastname": 
        if re.fullmatch(REG_EXP_NAME,value):
            return True
    elif validation_type == "email":
        if re.fullmatch(REG_EXP_EMAIL,value):
            return True
    elif validation_type == "username":
        if re.fullmatch(REG_EXP_USERNAME,value):
            return True
    
    return False

# retona -1 cuando los valores en los campos no cumples con las condicionees de una password
# retorna 0 cuando cambas cumplen pero no son contresenias iguales
# retorna 1 cuando son constrasenias iguales y cumplen con los requisitos 
def validate_password(password:str, confirm_password:str):
    
    if re.fullmatch(REG_EXP_PASSWORD,password) and re.fullmatch(REG_EXP_PASSWORD, confirm_password):
        if password == confirm_password:
            return 1
        
        return 0
    else:
        return -1

def generate_account_number():

    n = random.randint(1, 999_999_999)

    return f"{n:012d}" # se le indica que formatee n, si n no cumple con 12 digitos rellena con 0 a la izquierda, la d indica decimal