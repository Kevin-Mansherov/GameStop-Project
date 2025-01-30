// function to get all books from the API
async function getGames() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/games');
        const gamesList = document.getElementById('games-list');
        gamesList.innerHTML = ''; // Clear existing list

        response.data.games.forEach(game => {
            gamesList.innerHTML += `
                <div class="game-card">
                    <h3>${game.title}</h3>
                    <p>Creator: ${game.creator}</p>
                    <p>Year: ${game.year_published}</p>
                    <p>Type: ${game.type}</p>
                </div>
            `;
        });
    } catch (error) {
        console.error('Error fetching games:', error);
        alert('Failed to load games');
    }
}
// function to add a new book to the database
async function addGame() {
    const title = document.getElementById('game-title').value;
    const creator = document.getElementById('game-creator').value;
    const year_published = document.getElementById('game-year-published').value;
    const type = document.getElementById('game-type').value;

    try {
        await axios.post('http://127.0.0.1:5000/games', {
            title: title,
            creator: creator,
            year_published: year_published,
            type: type
        });
        
        // Clear form fields
        document.getElementById('game-title').value = '';
        document.getElementById('game-creator').value = '';
        document.getElementById('game-year-published').value = '';
        document.getElementById('game-type').value = '';

        // Refresh the books list
        getGames();
        
        alert('Game added successfully!');
    } catch (error) {
        console.error('Error adding game:', error);
        alert('Failed to add game');
    }
}
async function getUsers() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/users');
        const gamesList = document.getElementById('users-list');
        gamesList.innerHTML = ''; // Clear existing list

        response.data.games.forEach(user => {
            gamesList.innerHTML += `
                <div class="game-card">
                    <h3>${user.id}</h3>
                    <p>Creator: ${user.name}</p>
                    <p>Year: ${user.email}</p>
                    <p>Type: ${user.password}}</p>
                </div>
            `;
        });
    } catch (error) {
        console.error('Error fetching users:', error);
        alert('Failed to load users');
    }
}
async function addUser() {
    const id = document.getElementById('user-id').value;
    const name = document.getElementById('user-name').value;
    const email = document.getElementById('user-email').value;
    const password = document.getElementById('user-password').value;

    try {
        await axios.post('http://127.0.0.1:5000/users', {
            id: id,
            name:name,
            email:email,
            password:password
        });
        
        // Clear form fields
        document.getElementById('user-id').value = '';
        document.getElementById('user-name').value = '';
        document.getElementById('user-email').value = '';
        document.getElementById('user-password').value = '';

        // Refresh the books list
        
        
        alert('User added successfully!');
    } catch (error) {
        console.error('Error adding user:', error);
        alert('Failed to add user');
    }
}





// Load all books when page loads
document.addEventListener('DOMContentLoaded', getGames);