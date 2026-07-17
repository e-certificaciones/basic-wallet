from flask import render_template, request, redirect, url_for, session
from app.auth import auth_bp # importar el objeto BluePrint

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    return render_template("/auth/login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    return render_template("/auth/register.html")

@auth_bp.route("/logout")
def logout():

    return "logout"