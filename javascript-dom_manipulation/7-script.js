document.addEventListener('DOMContentLoaded', () => {
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(rep => rep.json())
    .then(data => {
        const movies = data.results;
        const moviesList = document.getElementById('list_movies')
            movies.forEach(movie => {
                const ul = document.createElement('li');
                ul.textContent = movie.title;
                moviesList.appendChild(ul);
            })
        })
        .catch(error => console.error('Error:', error));
    })
