# create a __init__.py file in the models folder to make all the model act as a package if you dont have it already , also you can make one file with all the models just copy ythe all the code in the files into it

from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,auto_increment = True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(10),nullable=False)



