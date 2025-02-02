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
                    <p>Price: ${game.price}</p>
                    <p>Available: ${game.available}</p>
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
    const price = document.getElementById('game-price').value;
    const available = document.getElementById('amount-to-add').value;

    try {
        await axios.post('http://127.0.0.1:5000/games', {
            title: title,
            creator: creator,
            year_published: year_published,
            type: type,
            price:price,
            available:available
        });
        
        // Clear form fields
        document.getElementById('game-title').value = '';
        document.getElementById('game-creator').value = '';
        document.getElementById('game-year-published').value = '';
        document.getElementById('game-type').value = '';
        document.getElementById('game-price').value = '';
        document.getElementById('amount-to-add').value = '';

        // Refresh the books list
        getGames();
        
        alert('Game added successfully!');
    } catch (error) {
        console.error('Error adding game:', error);
        alert('Failed to add game');
    }
}
async function deleteGame() {
//******************************************* */
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
                    <p>Name: ${user.name}</p>
                    <p>Email: ${user.email}</p>
                    <p>Password: ${user.password}}</p>
                </div>
            `;
        });
    } catch (error) {
        console.error('Error fetching users:', error);
        alert('Failed to load users');
    }
}
async function getCustomers(){
    try {
        const response = await axios.get('http://127.0.0.1:5000/customers');
        const gamesList = document.getElementById('customers-list');
        gamesList.innerHTML = ''; // Clear existing list

        response.data.games.forEach(customer => {
            gamesList.innerHTML += `
                <div class="game-card">
                    <h3>${customer.id}</h3>
                    <p>Name: ${customer.name}</p>
                    <p>Phone Number: ${customer.phone_number}</p>
                    <p>City: ${customer.city}</p>
                    <p>Age: ${customer.age}</p>
                    <p>Loan ID: ${customer.loan_id}</p>
                </div>
            `;
        });
    } catch (error) {
        console.error('Error fetching users:', error);
        alert('Failed to load users');
    }
}
async function addCustomer(){
    const id = document.getElementById('customer-id').value;
    const name = document.getElementById('customer-name').value;
    const phone_number = document.getElementById('customer-phone-number').value;
    const city = document.getElementById('customer-city').value;
    const age = document.getElementById('customer-age').value;
    const loan_id = document.getElementById('customer-loan-id').value;

    try {
        await axios.post('http://127.0.0.1:5000/customers', {
            id: id,
            name:name,
            phone_number: phone_number,
            city: city,
            age:age,
            loan_id,loan_id
        });
        
        // Clear form fields
        document.getElementById('customer-id').value = '';
        document.getElementById('customer-name').value = '';
        document.getElementById('customer-phone-number').value = '';
        document.getElementById('customer-city').value = '';
        document.getElementById('customer-age').value = '';
        document.getElementById('customer-loan-id').value = '';
        
        getCustomers();
        alert('Customer added successfully!');
    } catch (error) {
        console.error('Error adding customer:', error);
        alert('Failed to add customer');
    }
}
async function deleteCustomer(){
// ******************************
}
async function getLoans(){
    try {
        const response = await axios.get('http://127.0.0.1:5000/loans');
        const loansList = document.getElementById('loans-list');
        loansList.innerHTML = ''; // Clear existing list

        response.data.games.forEach(loan => {
            loansList.innerHTML += `
                <div class="loan-card">
                    <h3>${loansList.id}</h3>
                    <p>Customer ID: ${loan.customer_id}</p>
                    <p>Game ID: ${loan.game_id}</p>
                    <p>Loan date: ${loan.loan_date}</p>
                    <p>Return date: ${loan.return_date}</p>
                </div>
            `;
        });
    } catch (error) {
        console.error('Error fetching loans:', error);
        alert('Failed to load loans');
    }
}

async function addLoan(){
    const id = document.getElementById('loan-id').value;
    const customer_id = document.getElementById('loan-customer-id').value;
    const game_id = document.getElementById('loan-game-id').value;
    const loan_date = document.getElementById('loan-loan-date').value;
    const return_date = document.getElementById('loan-return-date').value;

    try {
        await axios.post('http://127.0.0.1:5000/loans', {
            id:id,
            customer_id:customer_id,
            game_id:game_id,
            loan_date:loan_date,
            return_date:return_date
        });
        
        // Clear form fields
        document.getElementById('loan-id').value = '';
        document.getElementById('loan-customer-id').value = '';
        document.getElementById('loan-game-id').value = '';
        document.getElementById('loan-loan-date').value = '';
        document.getElementById('loan-return-date').value = '';

        // Refresh the books list
        getLoans()
        
        alert('Loan added successfully!');
    } catch (error) {
        console.error('Error adding loan:', error);
        alert('Failed to add loan');
    }
}

async function deleteLoan(){
// *****************************
}
async function login(){
    const emailInput = document.getElementById('email').value;
    const passwordInput = document.getElementById('password').value;

    axios.post('http://127.0.0.1:5000/login',{
        email:emailInput,
        password:passwordInput
    },{
        Headers:{
            "Content-Type":"application/json"
        }
    })
    .then(response=>{
        alert(response.data.message);
        document.getElementById("auth-section").classList.add("hidden");
        document.getElementById("main-section").classList.remove("hidden");
    })
    .catch(error=>{
        alert(error.response.data.error);
    })
}
async function logout(){
    axios.post('http://127.0.0.1:5000/logout').then(response=>{
        alert(response.data.message);
        document.getElementById("auth-section").classList.remove("hidden");
        document.getElementById("main-section").classList.add("hidden");
    })
    .catch(error=>{
        alert('Failed to logout: ' + error.response.data.error);
    })
}

// Load all books when page loads
document.addEventListener('DOMContentLoaded', getGames);