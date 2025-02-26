from flask import Blueprint

order_bp = Blueprint('orders', __name__)

@order_bp.route('/order', methods=['POST'])
def test_route():
    return {"message": "Order route is working!"}
