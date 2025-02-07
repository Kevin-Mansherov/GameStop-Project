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
                    <button type="button" onclick="deleteGame(${game.id})">Delete Game</button>
                    <button type="button" onclick="moveEditScreen(${game.id},
                     '${game.title}', '${game.creator}', '${game.year_published}', '${game.type}', '${game.price}')">Edit Game</button>
                </div>
            `;
        });
    } catch (error) {
        console.error('Error fetching games:', error);
        alert('Failed to load games');
    }
}
// function to add a new book to the database
async function addGame() 
{
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
async function deleteGame(game_id) {
    try{
        const confirmed = confirm("You sure you want to delete this game???");
        if(!confirmed) return;
        await axios.delete(`http://127.0.0.1:5000/games/${game_id}`);
        alert(response.data.message)
        getGames();
    }
    catch(error){
        console.error('Error trying to delete: ', error);
        alert(error.response.data.error);
    }
}
async function moveEditScreen(game_id,title,creator,year_published,type,price) {
    document.getElementById('main-section').classList.add('hidden');
    document.getElementById('edit-game').classList.remove('hidden');

    document.getElementById('game-id').value = game_id;
    
    document.getElementById('edit-title').value = title;
    document.getElementById('edit-creator').value = creator;
    document.getElementById('edit-year-published').value = year_published;
    document.getElementById('edit-type').value = type;
    document.getElementById('edit-price').value = price;
}
async function editGame() {
    try{
        const confirmed = confirm("You sure you want to make this changes?");
        if(!confirmed) return;

        const game_id = document.getElementById("Game-id").value;
        const updatedGame = {
            title: document.getElementById('edit-title').value,
            creator: document.getElementById('edit-creator').value,
            year_published: document.getElementById('edit-year-published').value,
            type: document.getElementById('edit-type').value,
            price: document.getElementById('edit-price').value
        };


        const response = await axios.put(`http://127.0.0.1:5000/games/${game_id}`,updatedGame);
        document.getElementById('main-section').classList.remove('hidden');
        document.getElementById('edit-game').classList.add('hidden');
        alert(response.data.message)
        getGames();
    }
    catch(error){
        console.error('Error trying to edit: ', error);
        alert(error.response.data.error);
    }
}
async function getUsers() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/users');
        const gamesList = document.getElementById('users-list');
        gamesList.innerHTML = ''; // Clear existing list

        response.data.users.forEach(user => {
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
        const customersList = document.getElementById('customers-list');
        customersList.innerHTML = ''; // Clear existing list

        response.data.customers.forEach(customer => {
            customersList.innerHTML += `
                <div class="game-card">
                    <h3>${customer.id}</h3>
                    <p>Name: ${customer.name}</p>
                    <p>Phone Number: ${customer.phone_number}</p>
                    <p>City: ${customer.city}</p>
                    <p>Age: ${customer.age}</p>
                    <button type="button" onclick="deleteCustomer(${customer.id})">Delete Customer</button>
                </div>
            `;
        });
    } catch (error) {
        alert(error.response.data.error);
    }
}
async function addCustomer(){
    const id = document.getElementById('customer-id').value;
    const name = document.getElementById('customer-name').value;
    const phone_number = document.getElementById('customer-phone-number').value;
    const city = document.getElementById('customer-city').value;
    const age = document.getElementById('customer-age').value;

    try {
        await axios.post('http://127.0.0.1:5000/customers', {
            id: id,
            name:name,
            phone_number: phone_number,
            city: city,
            age:age
        });
        
        // Clear form fields
        document.getElementById('customer-id').value = '';
        document.getElementById('customer-name').value = '';
        document.getElementById('customer-phone-number').value = '';
        document.getElementById('customer-city').value = '';
        document.getElementById('customer-age').value = '';
        
        getCustomers();
        alert('Customer added successfully!');
    } catch (error) {
        console.error('Error adding customer:', error);
        alert('Failed to add customer');
    }
}
async function deleteCustomer(customer_id){
    try{
        const confirmed = confirm("You sure you want to delete this Customer???");
        if(!confirmed) return;
        await axios.delete(`http://127.0.0.1:5000/customers/${customer_id}`);
        alert(response.data.message)
        getCustomers();
    }
    catch(error){
        console.error('Error trying to delete: ', error);
        alert(error.response.data.error);
    }
}
async function getLoans(){
    try {
        const response = await axios.get('http://127.0.0.1:5000/loans');
        const loansList = document.getElementById('loans-list');
        loansList.innerHTML = ''; // Clear existing list

        response.data.loans.forEach(loan => {
            loansList.innerHTML += `
                <div class="loan-card">
                    <h3>${loan.id}</h3>
                    <p>Customer ID: ${loan.customer_id}</p>
                    <p>Game ID: ${loan.game_id}</p>
                    <p>Loan date: ${loan.loan_date}</p>
                    <p>Return date: ${loan.return_date}</p>
                    <button type="button" onclick="deleteLoan(${loan.id})">Delete Loan</button>
                </div>
            `;
        });
    } catch (error) {
        alert(error.response.data.error);
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

async function deleteLoan(loan_id){
    try{
        const confirmed = confirm("You sure you want to delete this loan???");
        if(!confirmed) return;
        await axios.delete(`http://127.0.0.1:5000/loans/${loan_id}`);
        alert(response.data.message)
        getLoans();
    }
    catch(error){
        console.error('Error trying to delete: ', error);
        alert(error.response.data.error);
    }
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
        localStorage.setItem('isLoggedIn','true');
        alert(response.data.message);
        document.getElementById("auth-section").classList.add("hidden");
        document.getElementById("main-section").classList.remove("hidden");
    })
    .catch(error=>{
        alert(error.response.data.error);
    })
}
async function logout(){
    localStorage.removeItem('isLoggedIn');
    document.getElementById("auth-section").classList.remove("hidden");
    document.getElementById("main-section").classList.add("hidden");
    alert(response.data.message);
}
function checkIfLoggedIn(){
    const isLoggedIn = localStorage.getItem('isLoggedIn');
    if(isLoggedIn == 'true'){
        document.getElementById("auth-section").classList.add("hidden");
        document.getElementById("main-section").classList.remove("hidden");
        getGames();
    }
    else{
        document.getElementById("auth-section").classList.remove("hidden");
        document.getElementById("main-section").classList.add("hidden");
    }
}
window.onload = ()=>{
    checkIfLoggedIn();
    getCustomers();
    getLoans();
}
    // Load all books when page loads
document.addEventListener('DOMContentLoaded', getGames);