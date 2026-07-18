'use strict'

document.addEventListener('DOMContentLoaded', function(){

     // incluimos numeros del 0-9, puntos y guiones, pero no deben tener espacios 
    const reg_exp_user = /^[a-zA-Z0-9_áéíóúÁÉÍÓÚñÑ.-]+$/

    // no se permiten caracteres especiales que no sean ._- ademas el minimo es de 6 caracteres
    const reg_exp_password = /^[a-zA-Z0-9._-]{6,}$/

    const form = document.querySelector('#form-login');

    // validar campos recibe la expresion regular, el valor a valida, el id parrafo para mostrar el mensaje de error
    // y el parametro message se refiere al nombre del campo que queremos guardar
    function validate_input(regular_expresion, value, p_id, message)
    {
        var paragraph = document.querySelector(p_id); 
        
        if (!regular_expresion.test(value)) // las expresiones regulares traen por defecto la funcion test
        {
            paragraph.innerHTML = ""; // limpiar para no mostrar mensajes de error repetidos
            let text = `must provide <b>${message}</b>.`;

            paragraph.innerHTML = text;
            paragraph.style.color = "red";

            return false;
        }
        
        paragraph.innerHTML = "";
        return true;
    }

    form.addEventListener('submit', (e)=>{
        console.log('submit')
        e.preventDefault();
        var validated = true;
        var username = document.querySelector('#username').value.trim();
        var password = document.querySelector('#password').value.trim();

        if (!validate_input(reg_exp_user,username,'#error-username',"valid username")) {validated = false;}
        if (!validate_input(reg_exp_password,password,'#error-password', "valid password")) {validated = false;}

        
        if (validated)
        {
            form.submit();
        }
        
    });

});