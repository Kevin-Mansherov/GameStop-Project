from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
from models import db
from models.user import User
from models.customers import Customers
from models.games import Game
from models.loans import Loan


app = Flask(__name__)  # - create a flask instance
# - enable all routes, allow requests from anywhere (optional - not recommended for security)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = "superSecretKey"

# Specifies the database connection URL. In this case, it's creating a SQLite database
# named 'library.db' in your project directory. The three slashes '///' indicate a
# relative path from the current directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///GameStore.db'
db.init_app(app)  # initializes the database with the flask application


# this is a decorator from the flask module to define a route for for adding a book, supporting POST requests.(check the decorator summary i sent you and also the exercises)
@app.route('/games', methods=['POST'])
def add_game():
    data = request.json  # this is parsing the JSON data from the request body
    new_game = Game(
        title=data['title'],  # Set the title of the new book.
        creator=data['creator'],  # Set the author of the new book.
        year_published=data['year_published'],
        # Set the types(fantasy, thriller, etc...) of the new book.
        type=data['type'],
        # add other if needed...
        price=data['price'],
        available=data['available']
    )
    db.session.add(new_game)  # add the bew book to the database session
    db.session.commit()  # commit the session to save in the database
    return jsonify({'message': 'Game added to database.'}), 201

# a decorator to Define a new route that handles GET requests
@app.route('/games', methods=['GET'])
def get_games():
    try:
        games = Game.query.all()                    # Get all the books from the database

        # Create empty list to store formatted book data we get from the database
        games_list = []

        for game in games:                         # Loop through each book from database
            game_data = {                          # Create a dictionary for each book
                'id': game.id,
                'title': game.title,
                'creator': game.creator,
                'year_published': game.year_published,
                'type': game.type,
                'price':game.price,
                'available':game.available
            }
            # Add the iterated book dictionary to our list
            games_list.append(game_data)

        return jsonify({                           # Return JSON response
            'message': 'Games retrieved successfully',
            'games': games_list
        }), 200

    except Exception as e:
        return jsonify({
            'error': 'Failed to retrieve games',
            'message': str(e)
        }), 500                                    #

@app.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    try:
        game = Game.query.get(game_id)
        if not game:
            return jsonify({
                'error': 'Game not found',
                'message':f'There is not game called {game_id}'
            }),404
        db.session.delete(game)
        db.session.commit()
        return jsonify({'message': f'{game_id} deleted from database.'}),200
    except Exception as e:
        return jsonify({
            'error': f'Failed to delete game {game_id}',
            'message': str(e)
        }),500

@app.route('/games/<int:game_id>', methods=['PUT'])
def edit_game(game_id):
    try:
        data = request.json
        game = Game.query.get(game_id)
        
        game.title = data['title']
        game.creator = data['creator']
        game.year_published = data['year_published']
        game.type = data['type']
        game.price = data['price']
        game.available = data['available']
        db.session.commit()

        return jsonify({'message': 'Changes saved successfully.'}),201
    except Exception as e:
        return jsonify({'error':str(e)}),404
    



@app.route('/users', methods=['POST'])
def add_user():
    data = request.json  # this is parsing the JSON data from the request body
    new_user = User(
        name=data['name'],
        email=data['email'],
        password=data['password']
    )
    db.session.add(new_user)  # add the bew book to the database session
    db.session.commit()  # commit the session to save in the database
    return jsonify({'message': 'User added to database.'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()                    # Get all the books from the database

        # Create empty list to store formatted book data we get from the database
        users_list = []

        for user in users:                         # Loop through each book from database
            user_data = {                          # Create a dictionary for each book
                'id': user.id,
                'name': user.name,
                'email' : user.email,
                'password' : user.password
            }
            # Add the iterated book dictionary to our list
            users_list.append(user_data)

        return jsonify({                           # Return JSON response
            'message': 'Users retrieved successfully',
            'users': users_list
        }), 200

    except Exception as e:
        return jsonify({
            'error': 'Failed to retrieve users',
            'message': str(e)
        }), 500




@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json  # this is parsing the JSON data from the request body
    new_customer = Customers(
        id=data['id'],
        name=data['name'],
        phone_number=data['phone_number'],
        city=data['city'],
        age=data['age']
    )
    db.session.add(new_customer)  # add the bew book to the database session
    db.session.commit()  # commit the session to save in the database
    return jsonify({'message': 'Customer added to database.'}), 201

@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        customers = Customers.query.all()                    # Get all the books from the database

        # Create empty list to store formatted book data we get from the database
        customers_list = []

        for customer in customers:                         # Loop through each book from database
            user_data = {                          # Create a dictionary for each book
                'id': customer.id,
                'name': customer.name,
                'phone_number': customer.phone_number,
                'city': customer.city,
                'age': customer.age
            }
            # Add the iterated book dictionary to our list
            customers_list.append(user_data)

        return jsonify({                           # Return JSON response
            'message': 'Customers retrieved successfully',
            'customers': customers_list
        }), 200

    except Exception as e:
        return jsonify({
            'error': 'Failed to retrieve customers',
            'message': str(e)
        }), 500

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        customer = Customers.query.get(customer_id)
        if not customer:
            return jsonify({'error': 'Loan not found','message':f'There is not loan with the id {customer_id}'}),404
        
        db.session.delete(customer)
        db.session.commit()
        return jsonify({'message': f'Customer {customer_id} deleted from database.'}),200
    except Exception as e:
        return jsonify({
            'error': f'Failed to delete customer {customer_id}',
            'message': str(e)
        }),500

@app.route('/customers/<int:customer_id>', methods=['PUT'])
def edit_customer(customer_id):
    try:
        data = request.json
        customer = Customers.query.get(customer_id)

        customer.name = data['name']
        customer.phone_number = data['phone_number']
        customer.city = data['city']
        customer.age = data['age']
        db.session.commit()

        return jsonify({'message': 'Changes saved successfully.'}),201
    except Exception as e:
        return jsonify({'error':str(e)}),404



@app.route('/loans', methods=['POST'])
def add_loan():
    data = request.json
    customer = Customers.query.get(data['customer_id'])
    if not customer:
        return jsonify({'error':'Customer is not found.'}),404
    new_loan = Loan(
        id = data['id'],
        customer_id = data['customer_id'],
        game_id = data['game_id'],
        loan_date = datetime.strptime(data['loan_date'], "%Y-%m-%d"),
        return_date = datetime.strptime(data['return_date'], "%Y-%m-%d"),
    )
    game = Game.query.get(data['game_id'])
    if game:
        game.available-=1
        db.session.add(new_loan)
        db.session.commit()
        db.session.refresh(game)
        return jsonify({'message': 'Loan added to database.'}), 201
    else:
        return jsonify({'error':'Game not found'}),404
    
@app.route('/loans', methods=['GET'])
def get_loans():
    try:
        loans = Loan.query.all()
        loans_list = []
        for loan in loans:
            loan_data = {
                'id': loan.id,
                'customer_id': loan.customer_id,
                'game_id': loan.game_id,
                'loan_date': loan.loan_date,
                'return_date': loan.return_date
            }
            loans_list.append(loan_data)
        return jsonify({                           # Return JSON response
            'message': 'Loans retrieved successfully',
            'loans': loans_list
        }), 200
    except Exception as e:
        return jsonify({
            'error': 'Failed to retrieve loans',
            'message': str(e)
        }), 500

@app.route('/loans/<int:loan_id>', methods=['DELETE'])
def delete_loan(loan_id):
    try:
        loan = Loan.query.get(loan_id)
        if not loan:
            return jsonify({
                'error': 'Loan not found',
                'message':f'There is not loan with the id {loan_id}'
            }),404
        game = Game.query.get(loan.game_id)
        if game:
            game.available+=1           
            db.session.delete(loan)
            db.session.commit()
            db.session.refresh(game)
            return jsonify({'message': f'Loan {loan_id} deleted from database.'}),200
    except Exception as e:
        return jsonify({
            'error': f'Failed to delete loan {loan_id}',
            'message': str(e)
        }),500





@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user_email = data['email']
    user_password = data['password']
    user = User.query.filter_by(email = user_email,password = user_password).first()
    if user:
        return jsonify({'message':'Login successful'}),200
    else:
        return jsonify({'error': 'Invalid email or password.'}),401

@app.route('/logout', methods=['POST']) 
def logout():
    return jsonify({'message': 'You are logout.'}),200


if __name__ == '__main__':
#     with app.app_context():
#         db.drop_all()
#         db.create_all()  # Create all database tables defined in your  models(check the models folder)

# # ***add data to the users api
#     with app.test_client() as test_client:
#             response = test_client.post('/users', json={
#                 "name": "Kevin Mansherov",
#                 "email": "kevin@gmail.com",
#                 "password": "123"
#             })
#             print(response.status_code)
#             print(response.get_json())

    # with app.test_client() as test:
    #     response = test.post('/books', json={  # Make a POST request to /books endpoint with book  data
    #         'title': 'Harry Potter',
    #         'author': 'J.K. Rowling',
    #         'year_published': 1997,
    #         'types': '1'  # lets say 1 is fantasy
    #     })
    #     print("Testing /books endpoint:")
    #     # print the response from the server
    #     print(f"Response: {response.data}")

    #     #  GET test here
    #     get_response = test.get('/books')
    #     print("\nTesting GET /books endpoint:")
    #     print(f"Response: {get_response.data}")

    app.run(debug=True)  # start the flask application in debug mode

    # DONT FORGET TO ACTIVATE THE ENV FIRST:
    # /env/Scripts/activate - for windows
    # source ./env/bin/activate - - mac