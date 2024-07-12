document.addEventListener('DOMContentLoaded', () => {
  const rawgApiKey = '43007c6d95384db8805db9bb47422309';
  const youtubeApiKey = 'AIzaSyDPzFfPZLli38CuOacjfnCNLRwZjmqTafU';
  const gameNames = [
      "What Lies in the Multiverse", "Pixel Noir", "Super Trench Attack!",
      "Hero Siege", "Rise of Jericho",
      "Clash: Artifacts of Chaos", "The Eightfold Path",
     "Kenosis: The Liminal Tapes",
      "Tormented Souls", 
  ];

  const fetchGameData = (name) => {
      return fetch(`https://api.rawg.io/api/games?key=${rawgApiKey}&search=${encodeURIComponent(name)}`)
          .then(response => response.json())
          .then(data => {
              if (data.results.length > 0) {
                  return data.results[0];
              }
              throw new Error(`Game not found: ${name}`);
          });
  };

  const fetchGameTrailer = (id) => {
      return fetch(`https://api.rawg.io/api/games/${id}/youtube?key=${rawgApiKey}`)
          .then(response => response.json())
          .then(data => {
              if (data.results.length > 0) {
                  return data.results[0].external_id;
              }
              return null;
          });
  };

  const displayGame = async (game) => {
      const gamesContainer = document.getElementById('games');

      const gameElement = document.createElement('div');
      gameElement.classList.add('game');

      const trailerId = await fetchGameTrailer(game.id);
      const trailerUrl = trailerId ? `https://www.youtube.com/embed/${trailerId}?key=${youtubeApiKey}` : '';

      gameElement.innerHTML = `
          <h2>${game.name}</h2>
          <img src="${game.background_image}" alt="${game.name}">
          <p><strong>Description:</strong> ${game.description_raw}</p>
          <p><strong>Developer:</strong> ${game.developers[0].name}</p>
          ${trailerUrl ? `<iframe src="${trailerUrl}" frameborder="0" allowfullscreen></iframe>` : ''}
      `;

      gamesContainer.appendChild(gameElement);
  };

  gameNames.forEach(gameName => {
      fetchGameData(gameName)
          .then(game => displayGame(game))
  });
});
const fetchGameTrailer = (id) => {
  return fetch(`https://api.rawg.io/api/games/${id}/youtube?key=${rawgApiKey}`)
      .then(response => {
          if (!response.ok) {
              throw new Error(`Error fetching trailer: ${response.statusText}`);
          }
          return response.json();
      })
      .then(data => {
          if (data.results.length > 0) {
              return data.results[0].external_id;
          }
          return null;
      })
      .catch(error => {
          console.error(error);
          throw error; 
      });
};