from .repository import add_customer, delete_customer, get_customers, get_customer
from .models import Customer

def create_customer(first_name, last_name):
    customer = Customer(first_name=first_name, last_name=last_name)
    add_customer(customer)

def remove_customer(customer_id):
    delete_customer(customer_id)

def get_all_customers():
    return get_customers()

def get_customer_by_id(customer_id):
    return get_customer(customer_id)
