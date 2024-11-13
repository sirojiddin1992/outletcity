from flask import Blueprint, request, jsonify
from models.shop import Shop, Discount
from app import db
from flask_jwt_extended import jwt_required

shop_bp = Blueprint('shop', __name__)

@shop_bp.route('/', methods=['POST'])
@jwt_required()
def create_shop():
    data = request.get_json()
    new_shop = Shop(name=data['name'], address=data['address'], contact=data['contact'], owner_id=data['owner_id'])
    db.session.add(new_shop)
    db.session.commit()
    return jsonify(message="Do'kon yaratildi"), 201

@shop_bp.route('/', methods=['GET'])
@jwt_required()
def get_shops():
    shops = Shop.query.all()
    return jsonify(shops=[shop.name for shop in shops]), 200
