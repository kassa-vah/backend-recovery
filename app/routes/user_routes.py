from flask import Blueprint, request, jsonify
from app.db import db
from app.models import User, Product, Order, OrderItem
from werkzeug.security import generate_password_hash, check_password_hash

user_bp = Blueprint("user", __name__)
product_bp = Blueprint("product", __name__)
order_bp = Blueprint("order", __name__)
orderitem_bp = Blueprint("orderitem", __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
   

  

    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if user and check_password_hash (user.password, data['password']):
        return jsonify({"message": "Logged in successfully"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


@product_bp.route("/products", methods=["POST"])
def create_products():
    data = request.get_json()

    new_product = Product(
        product_name=data['product_name'], 
        description=data['description'], 
        price=data['price'], 
        quantity=data['quantity'], 
        category=data['category'])
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product created successfully"}), 201

@orderitem_bp.route("/orderitem", methods=["POST"])
def create_order_item():
    data = request.get_json()

    new_order_item = OrderItem(
        order_id=data['order_id'], 
        product_id=data['product_id'], 
        quantity=data['quantity'], 
        price=data['price'])

    db.session.add(new_order_item)
    db.session.commit()



