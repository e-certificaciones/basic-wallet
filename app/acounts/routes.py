from flask import render_template, redirect, url_for, session
from app.acounts import acounts_bp # importar el blueprint
from app.acounts.models import index_information, calculate_send_recipient_money
from app.helpers import login_required

@acounts_bp.route("/")
@login_required
def index():
    
    user_id = session.get('user_id')
    
    data = index_information(user_id)

    send_money, recipient_money = calculate_send_recipient_money(user_id)

    return render_template("/acounts/index.html", data=data, send_money=send_money, recipient_money=recipient_money)

