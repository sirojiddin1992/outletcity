from flask import jsonify
from app import app, db
from models import Shop

@app.route('/api/shops', methods=['GET'])
def get_shops():
    shops = Shop.query.all()
    shop_list = []
    for shop in shops:
        shop_data = {
            'id': shop.id,
            'name': shop.name,
            'description': shop.description,
            'discount': shop.discount,
            'location': shop.location
        }
        shop_list.append(shop_data)
    return jsonify(shop_list)
