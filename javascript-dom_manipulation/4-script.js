document.querySelector('#add_item').addEventListener('click', function() {
    const li = document.createElement('li');
    li.innerHTML = 'Item';
    document.querySelector('ul.my_list').appendChild(li);
});