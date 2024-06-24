from .models import Customer
from . import db

def add_customer(customer):
    db.session.add(customer)
    db.session.commit()

def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer:
        db.session.delete(customer)
        db.session.commit()

def get_customers():
    return Customer.query.all()

def get_customer(customer_id):
    return Customer.query.get(customer_id)
