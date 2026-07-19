from flask import render_template, redirect, url_for, request, session
from app.helpers import login_required
from app.transactions import transactions_bp
from app.transactions.models import recipient_information, validate_diferent_acount_number, validate_suficient_balance

@transactions_bp.route("/send_money", methods=["GET", "POST"])
@login_required
def send_money():

    if request.method == "POST":
        
        step = request.form.get('step')

        if step == "lookup":

            data = {
                'acount_number' : request.form.get('acount-number')
            }

            error = {}

            if not validate_diferent_acount_number(data['acount_number'].strip(), session.get("user_id")):
                error['acount_number'] = "must provide valid acount number"

            if error:
                return render_template("/transactions/send_money.html", error=error, data=data)
            else:
                data_recipient = recipient_information(data['acount_number'])
    
                return render_template("/transactions/send_money.html", data=data, data_recipient=data_recipient, error={})
        
        elif step == "send":

            data = {
                'acount_number' : request.form.get('acount-number'),
                'amount' : request.form.get('amount').strip()
            }

            error = {}

            data_recipient = {
                'name' : request.form.get('name'),
                'last_name' : request.form.get('last_name')
            }


            if validate_suficient_balance(data['amount'], session.get('user_id')) == -1:
                error['amount'] = "must provide valid amount"
            elif validate_suficient_balance(data['amount'], session.get('user_id')) == 0:
                error['amount'] = "your balance is insuficiente"
            elif validate_suficient_balance(data['amount'], session.get('user_id')) == 1:
                print("enviando dinero...")
            
            return render_template("/transactions/send_money.html", data=data, data_recipient=data_recipient, error=error)


    return render_template("/transactions/send_money.html", error={}, data={})

@transactions_bp.route("/transfer", methods=["POST"])
@login_required
def transfer():

    return "probando"