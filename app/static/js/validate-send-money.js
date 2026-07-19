'use strict'

document.addEventListener('DOMContentLoaded', ()=>{

    // regular expresions

    // solo se permiten cadenas numericas de 12 digitos 
    const reg_exp_acount_number = /^[0-9]{12}$/;

    const form = document.querySelector('#lookup');
    const from_send = document.querySelector('#send');

    function validate_input(acount_number){

        var paragraph = document.querySelector('#error-acount-number');

        if (!reg_exp_acount_number.test(acount_number))
        {
            paragraph.innerHTML = "";
            let text = `must provide valid <b>acount_number</b>`;

            paragraph.innerHTML =  text;
            paragraph.style.color = "red";

            return false;
        }
        else
        {
            paragraph.innerHTML = "";

            return true;
        }
    }

    form.addEventListener('submit', function(e){
        
        e.preventDefault();

        var acount_number = document.querySelector('#acount-number').value.trim();
        var validated = true;

        if (!validate_input(acount_number)){validated = false;}        

        if (validated == true)
        {
            form.submit();
        }

    });

    from_send.addEventListener('submit', (e)=>{

        e.preventDefault();
        var amount = document.querySelector('#amount').value.trim();
        var paragraph_amount = document.querySelector('#error-amount');
        var validated = true;

        if (isNaN(amount) || amount.length == 0)
        {   
            paragraph_amount.innerHTML = "";
            let text = `must provide valid <b>amount</b>`;

            paragraph_amount.innerHTML = text;
            paragraph_amount.style.color = "red";
            validated = false;
        }
        else
        {
            paragraph_amount.innerHTML = "";
        }

        if (validated)
        {
            from_send.submit();
        }

    });
});