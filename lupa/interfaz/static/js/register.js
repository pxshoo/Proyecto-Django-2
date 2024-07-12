document.getElementById('register-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirm_password').value;
    var errorMessage = document.getElementById('error-message');

    errorMessage.textContent = '';

    if (!username || !email || !password || !confirmPassword) {
        errorMessage.textContent = 'Por favor, complete todos los campos.';
        return;
    }

    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailPattern.test(email)) {
        errorMessage.textContent = 'Por favor, ingrese un correo electrónico válido.';
        return;
    }

    if (password !== confirmPassword) {
        errorMessage.textContent = 'Las contraseñas no coinciden.';
        return;
    }else {

        alert("Registro completo. Redirigiendo a iniciar sesión...");
    }


    console.log('Registro exitoso');
    errorMessage.textContent = 'Registro exitoso';

    setTimeout(function() {
        window.location.href = '../login/';
    }, 2000); 
});
