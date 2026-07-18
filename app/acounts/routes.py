from flask import render_template, redirect, url_for, session
from app.acounts import acounts_bp # importar el blueprint
from app.acounts.models import index_information
from app.helpers import login_required

@acounts_bp.route("/")
@login_required
def index():
    
    user_id = session.get('user_id')
    
    data = index_information(user_id)

    return render_template("/acounts/index.html", data=data)


