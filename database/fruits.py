from flask import Blueprint, jsonify, request
from .models import Fruit
from . import db

fruit_blueprint = Blueprint('fruits', __name__)

@fruit_blueprint.route('/fruits', methods=['GET'])
def get_fruits():
    fruits = Fruit.query.all()
    return jsonify([{'id': fruit.id, 'name': fruit.name} for fruit in fruits])

@fruit_blueprint.route('/fruits', methods=['POST'])
def add_fruit():
    new_fruit = Fruit(name=request.json['name'])
    db.session.add(new_fruit)
    db.session.commit()
    return jsonify({'id': new_fruit.id, 'name': new_fruit.name})
