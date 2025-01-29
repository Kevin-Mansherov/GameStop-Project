from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
from models import db
from models.user import User
from models.games import Game
from models.loans import Loan


app = Flask(__name__)  # - create a flask instance
# - enable all routes, allow requests from anywhere (optional - not recommended for security)
CORS(app, resources={r"/*": {"origins": "*"}})


# Specifies the database connection URL. In this case, it's creating a SQLite database
# named 'library.db' in your project directory. The three slashes '///' indicate a
# relative path from the current directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///GameStore.db'
db.init_app(app)  # initializes the databsewith the flask application


# this is a decorator from the flask module to define a route for for adding a book, supporting POST requests.(check the decorator summary i sent you and also the exercises)
@app.route('/games', methods=['POST'])
def add_game():
    data = request.json  # this is parsing the JSON data from the request body
    new_game = Game(
        title=data['title'],  # Set the title of the new book.
        creator=data['creator'],  # Set the author of the new book.
        year_published=data['year_published'],
        # Set the types(fantasy, thriller, etc...) of the new book.
        type=data['type']
        # add other if needed...
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
                'type': game.type
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

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json  # this is parsing the JSON data from the request body
    new_user = User(
        id=data['id'],
        name=data['name'],
        phone_number=data['phone_number'],
        city=data['city'],
        age=data['age'],
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
                'phone_number': user.phone_number,
                'city': user.city,
                'age': user.age,
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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create all database tables defined in your  models(check the models folder)

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
