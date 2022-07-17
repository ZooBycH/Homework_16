from flask import jsonify, request
from models import *
from config import app
import utils
from service import init_db, insert_data_uni


@app.route('/users/', methods=['GET', 'POST'])
def views_users():
    if request.method == 'GET':
        return jsonify(utils.get_all(User))
    elif request.method == 'POST':
        insert_data_uni(User, [request.get_json()])
        return jsonify(request.get_json())


@app.route('/users/<int:uid>/', methods=['GET', 'PUT', 'DELETE'])
def views_user_id(uid):
    if request.method == 'GET':
        return jsonify(utils.get_by_id(User, uid))
    elif request.method == 'PUT':
        utils.update_user_uni(User, uid, request.json)
        return jsonify(["Ok"])
    elif request.method == 'DELETE':
        utils.delete_user_uni(User, uid)
        return "Данные удалены"


@app.route('/orders/', methods=['GET', 'POST'])
def views_orders():
    if request.method == 'GET':
        return jsonify(utils.get_all(Order))
    elif request.method == 'POST':
        insert_data_uni(Order, [request.get_json()])
        return jsonify(request.get_json())


@app.route('/orders/<int:oid>/', methods=['GET', 'PUT', 'DELETE'])
def views_order_id(oid):
    if request.method == 'GET':
        return jsonify(utils.get_by_id(Order, oid))
    elif request.method == 'PUT':
        utils.update_user_uni(Order, oid, request.json)
        return jsonify(["Ok"])
    elif request.method == 'DELETE':
        utils.delete_user_uni(Order, oid)
        return "Данные удалены"


@app.route('/offers/', methods=['GET', 'POST'])
def views_offers():
    if request.method == 'GET':
        return jsonify(utils.get_all(Offer))
    elif request.method == 'POST':
        insert_data_uni(Offer, [request.get_json()])
        return jsonify(request.get_json())


@app.route('/offers/<int:oid>/', methods=['GET', 'PUT', 'DELETE'])
def union_all_by_id(oid):
    if request.method == 'GET':
        return jsonify(utils.union_all_by_id(Offer, User, oid))
    elif request.method == 'PUT':
        utils.update_user_uni(Offer, oid, request.json)
        return jsonify(["Ok"])
    elif request.method == 'DELETE':
        utils.delete_user_uni(Offer, oid)
        return "Данные удалены"


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0')
