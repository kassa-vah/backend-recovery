from flask import Blueprint

orderitem_bp = Blueprint("orderitem", __name__)

@orderitem_bp.route("/orderitem", methods=["POST"])
def create_order_item():
    return {"message": "Order route is working!"}