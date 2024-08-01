from flask import Blueprint, jsonify, request
from .models import Legume
from . import db

legume_blueprint = Blueprint('legumes', __name__)

@legume_blueprint.route('/legumes', methods=['GET'])
def get_legumes():
    legumes = Legume.query.all()
    return jsonify([{'id': legume.id, 'name': legume.name} for legume in legumes])

@legume_blueprint.route('/legumes', methods=['POST'])
def add_legume():
    new_legume = Legume(name=request.json['name'])
    db.session.add(new_legume)
    db.session.commit()
    return jsonify({'id': new_legume.id, 'name': new_legume.name})
