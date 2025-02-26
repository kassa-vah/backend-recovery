from flask import Flask
from app import models
from app.db import db
from app.routes.user_routes import user_bp
from app.routes.product_routes import product_bp
from app.routes.order_routes import order_bp
from app.routes.orderitem_routes import orderitem_bp



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(order_bp, url_prefix='/api/orders')
    app.register_blueprint(orderitem_bp, url_prefix='/api/orderitems')


    return app
