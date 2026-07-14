import os
from dotenv import load_dotenv

'''
    este archivo define la configuracion general de la aplicacion Flask
'''

load_dotenv() # lee las variables del entorno .venv

class Config:
    # buscamos secret_key dentro de las variables de entorno, si no existe 
    # le asignamos una, la clave se usa par proteger las cookies, sesiones y datos firmados 
    SECRET_KEY = os.getenv("SECRET_KEY", "mustuseasecretkey")
    # la sesion expira cuando se cierra el navegador
    SESSION_PERMANENT = False
    # guarda las sesiones del lado del servidor  
    SESSION_TYPE = "filesystem"

    # DATABASE = "wallet.db"