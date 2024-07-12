var toggle = document.getElementById('container');
var body = document.querySelector('body');

toggle.onclick = function(){
    toggle.classList.toggle('active');
    body.classList.toggle('active');
    juegos.classList.toggle('active');
}

document.querySelector('.toggle').addEventListener('click', function() {
    var container = document.getElementById('container');
    var toggle = document.querySelector('.toggle');

    
    if (toggle.style.left === '1px') {
        toggle.style.left = container.offsetWidth - toggle.offsetWidth - 1 + 'px';
        
    } else {
        toggle.style.left = '1px';
    }
});

