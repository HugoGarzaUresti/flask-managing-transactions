from flask import request, jsonify, current_app as app
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
