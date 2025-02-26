from flask import Blueprint

product_bp = Blueprint('products', __name__)

@product_bp.route('/test', methods=['POST'])
def test_route():
    return {"message": "Product route is working!"}
