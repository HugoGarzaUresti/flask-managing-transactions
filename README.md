
# Flask Managing Transactions

This project demonstrates how to manage transactions in a Flask application using SQLAlchemy. It is an equivalent of the Spring Boot guide on managing transactions.

## Project Structure

```
flask-managing-transactions/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── repository.py
│   ├── service.py
│   └── routes.py
├── config.py
├── run.py
└── requirements.txt
```

## Setup

### 1. Create a Virtual Environment

Create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 2. Install Required Packages

Install the dependencies:

```sh
pip install -r requirements.txt
```

### 3. Initialize the Database

Open a Flask shell to initialize the database:

```sh
flask shell
```

In the shell, run:

```python
from app import db
db.create_all()
exit()
```

## Running the Application

Run the Flask application:

```sh
python run.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## API Endpoints

### Add a Customer

**URL:** `/customer`

**Method:** `POST`

**Request Body:**

```json
{
  "first_name": "John",
  "last_name": "Doe"
}
```

**Response:**

```json
{
  "message": "Customer added successfully!"
}
```

Example `curl` command:

```sh
curl -X POST http://127.0.0.1:5000/customer -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe"}'
```

### Delete a Customer

**URL:** `/customer/<int:customer_id>`

**Method:** `DELETE`

**Response:**

```json
{
  "message": "Customer deleted successfully!"
}
```

Example `curl` command:

```sh
curl -X DELETE http://127.0.0.1:5000/customer/1
```

### Get All Customers

**URL:** `/customers`

**Method:** `GET`

**Response:**

```json
[
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe"
  }
]
```

Example `curl` command:

```sh
curl -X GET http://127.0.0.1:5000/customers
```

### Get a Specific Customer

**URL:** `/customer/<int:customer_id>`

**Method:** `GET`

**Response:**

```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe"
}
```

Example `curl` command:

```sh
curl -X GET http://127.0.0.1:5000/customer/1
```

## Project Details

### Configuration

The configuration settings are defined in `config.py`:

```python
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### Models

The `Customer` model is defined in `app/models.py`:

```python
from . import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
```

### Repository

Repository functions for database operations are defined in `app/repository.py`:

```python
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
```

### Service

Service functions for business logic are defined in `app/service.py`:

```python
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
```

### Routes

API endpoints are defined in `app/routes.py`:

```python
from flask import request, jsonify
from . import app
from .service import create_customer, remove_customer, get_all_customers, get_customer_by_id

@app.route('/customer', methods=['POST'])
def add_customer_route():
    data = request.get_json()
    create_customer(data['first_name'], data['last_name'])
    return jsonify({"message": "Customer added successfully!"}), 201

@app.route('/customer/<int:customer_id>', methods=['DELETE'])
def delete_customer_route(customer_id):
    remove_customer(customer_id)
    return jsonify({"message": "Customer deleted successfully!"}), 200

@app.route('/customers', methods=['GET'])
def get_customers_route():
    customers = get_all_customers()
    return jsonify([customer.to_dict() for customer in customers]), 200

@app.route('/customer/<int:customer_id>', methods=['GET'])
def get_customer_route(customer_id):
    customer = get_customer_by_id(customer_id)
    if customer:
        return jsonify(customer.to_dict()), 200
    else:
        return jsonify({"message": "Customer not found"}), 404
```

### Running Script

The Flask application is run using `run.py`:

```python
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

## Conclusion

This project provides a basic example of how to manage transactions in a Flask application using SQLAlchemy. It includes creating and deleting customer records with transaction management. Feel free to expand on this project by adding more features or improving error handling.
