document.getElementById('toggle_header').addEventListener('click', function(){
    const header = document.getElementsByClassName('green')[0] || document.getElementsByClassName('red')[0]
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
    }
    else {
        header.classList.remove('green');
        header.classList.add('red');
    }
});