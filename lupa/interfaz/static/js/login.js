function redirectToPrueba() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;


    if (username.trim() !== "" && password.trim() !== "") {

        window.location.href = "../prueba/";
    } else {

        alert("Por favor, completa todos los campos.");
    }
}
document.querySelectorAll('.toggle-password').forEach(button => {
    button.addEventListener('click', function() {
        const passwordField = this.previousElementSibling;
        if (passwordField.type === 'password') {
            passwordField.type = 'text';
            this.textContent = 'Ocultar';
        } else {
            passwordField.type = 'password';
            this.textContent = 'Mostrar';
        }
    });
});