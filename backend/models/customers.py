from . import db


class Customers(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    loan_id = db.Column(db.Integer, db.ForeignKey('loans.id'),nullable=False)