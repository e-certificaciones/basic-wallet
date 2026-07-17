from flask import render_template, request, redirect, url_for, session
from app.auth import auth_bp # importar el objeto BluePrint
from app.auth.services import validate_input, validate_password

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    return render_template("/auth/login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        data = {
            'name' : request.form.get('input-name').strip(),
            'last_name' : request.form.get('input-last-name').strip(),
            'email' : request.form.get('input-email').strip(),
            'username' : request.form.get('input-username').strip(),
            'password' : request.form.get('input-password').strip(),
            'confirm_password' : request.form.get('input-confirm-password').strip(),
            'birthday' : request.form.get('input-birthday'),
            'checkbox' : request.form.get('checkbox')
        }

        error = {}

        if not validate_input(data['name'], "name"):
            error['name'] = "must provide valid name"

        if not validate_input(data['last_name'], "name"):
            error['last_name'] = "must provide valid last name"
        
        if not validate_input(data['email'], "email"):
            error['email'] = "must provide valid email"

        if not validate_input(data['username'], "username"):
            error['username'] = "must provide valid username"
        
        if validate_password(data['password'], data['confirm_password']) == -1:
            error['password'] = "must provide valid password with 6 caracters. Only letters, numbers, (.), (-), and (_) are allowed."
            error['confirm_password'] = "must provide valid password with 6 caracters. Only letters, numbers, (.), (-), and (_) are allowed."
        elif validate_password(data['password'], data['confirm_password']) == 0:
            error['password'] = "must provide the same password in both input"
            error['confirm_password'] = "must provide the same password in both input"

        if data['birthday'] == "":
            error['birthday'] = "must provide valid date"

        if data['checkbox'] is None: # las comparaciones para valores None se deben hacer con is None o is not NOne
            error['checkbox'] = "you must check the box to confirm your information is correct."

        if error:
            return render_template("/auth/register.html", data=data, error=error)
        else:
            return redirect(url_for('auth.login'))
    
    # pasamos un diccionario vacio de error en el get, la idea es poder usar jinja para buscar errores y poner sus valores 
    # el los p descriptivos de cada para cada campo input, como jinja no da errores si un valor que buscar no existe, solo no muestra nada
    # usamos esta tecnica para no usar if anidados y que las validaciones del js tambien funcionen, sin usar un if elif para mostrar las 
    # etiquetas p, esto no funciona para data
    return render_template("/auth/register.html", error={}) 

@auth_bp.route("/logout")
def logout():

    return "logout"