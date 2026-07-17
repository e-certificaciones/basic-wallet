'use strict'

document.addEventListener('DOMContentLoaded', () =>{

    /**
     * usamos una expresion regular para validar que los datos de entrada en los inputs solo sean caracteres permitidos
     * en este caso en nombre no acetamos numeros, tampoco caracteres especiales con los que la entrada podria ser convertida
     * en un script
     */

    // toma todo el string de ^ -- $ y lo que esta [] son los unicos caracteres permitidos , el signo + indica que la restriccion
    // debe funcionar para uno o mas caracteres 
    const reg_exp_name = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/;

    // despues del punto el minimo de caracteres que debe haber es 3 [a-zA-Z]{3,}
    const reg_exp_email = /^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{3,}$/;

    // incluimos numeros del 0-9, puntos y guiones, pero no deben tener espacios 
    const reg_exp_user = /^[a-zA-Z0-9_áéíóúÁÉÍÓÚñÑ.-]+$/

    // no se permiten caracteres especiales que no sean ._- ademas el minimo es de 6 caracteres
    const reg_exp_password = /^[a-zA-Z0-9._-]{6,}$/


    const form = document.querySelector('form');
    
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


    form.addEventListener('submit', function(e){
        e.preventDefault(); // evitamos que por defecto lo mande al action del form, primero debemos ver las validaciones

        var name = document.querySelector('#input-name').value.trim();
        var last_name = document.querySelector('#input-last-name').value.trim();
        var email = document.querySelector('#input-email').value.trim();
        var user_name = document.querySelector('#input-username').value.trim();
        var password = document.querySelector('#input-password').value.trim();
        var confirm_password = document.querySelector('#input-confirm-password').value.trim();
        var birthday = document.querySelector('#input-birthday').value;
        var check_box = document.querySelector('#checkbox');

        let form_value = true;

        if (!validate_input(reg_exp_name, name, '#error-name', "name")){form_value = false;} // validar input de name
        
        if (!validate_input(reg_exp_name, last_name, '#error-last-name', "last name")){form_value = false;} // validar input de last name 

        if (!validate_input(reg_exp_email, email, '#error-email', "email")){ form_value = false;} // validar el email

        if (!validate_input(reg_exp_user, user_name, '#error-username', "username")){form_value = false} // validar el username

        // validacion de contraseñas
        if (validate_input(reg_exp_password,password,'#error-password', "password with 6 caracters. Only letters, numbers, (.), (-), and (_) are allowed.") &&
            validate_input(reg_exp_password,confirm_password, '#error-confirm-password',"password Only letters, numbers, (.), (-), and (_) are allowed."))
        {
            if (password === confirm_password)
            {
                form_value = true;
            }
            else
            {
                form_value = false;
            }
        }
        
               
        if (birthday === "")
        {
            let paragraph = document.querySelector('#error-calendar'); 
            paragraph.innerHTML = ""; // limpiar para no mostrar mensajes de error repetidos
            let text = `must provide <b>date</b>.`;

            paragraph.innerHTML = text;
            paragraph.style.color = "red";

            form_value = false;
        }
        else
        {
            document.querySelector('#error-calendar').innerHTML = ""; 
        }

        if(check_box.checked && form_value) // check_box.check retorna un value bool
        {
            form.submit();
        }
        else
        {
            let paragraph = document.querySelector('#error-checkbox'); 
               
            paragraph.innerHTML = ""; // limpiar para no mostrar mensajes de error repetidos
            let text = `must provide checked while you muth provides all data`;

            paragraph.innerHTML = text;
            paragraph.style.color = "red";

            form_value = false;
        }
        

    });


});