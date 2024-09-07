from flask import Blueprint, jsonify, request
from extensions import db, ma, mail, jwt, Message
from database.users import User, user_schema, users_schema 
from random import randint
from flask_mail import Message

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    results = users_schema.dump(all_users)
    return jsonify(results)

@main_bp.route('/users/<id>/', methods=['GET'])
def post_details(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

@main_bp.route('/add_user', methods=['POST'])
def add_user():
    email = request.json['email']
    password = request.json['password']
    users = User(email, password)
    db.session.add(users)
    db.session.commit()
    return user_schema.jsonify(users)

@main_bp.route('/update/<id>/', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    email = request.json['email']
    password = request.json['password']
    user.email = email
    user.password = password

    db.session.commit()
    return user_schema.jsonify(user)

@main_bp.route('/delete/<id>/', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)

@main_bp.route('/reset_password', methods=['POST'])
def reset_password():
    # data = request.get_json()
    # user = User.query.filter_by(email=data['email']).first()

    # if not user:
    #     return jsonify({'message': 'Email does not exist'}), 404

    # new_password = 'temporary_password'  # Vous pouvez générer un mot de passe temporaire plus complexe si nécessaire
    # if new_password:
    #     hashed_password = generate_password_hash(new_password, method='sha256')
    #     user.password = hashed_password
    #     db.session.commit()

    #     # Envoi du mail
    #     msg = Message('Password Reset Request',
    #                   sender='anisahrab043@gmail.com',
    #                   recipients=[user.email])
    #     msg.body = f'Your new temporary password is: {new_password}'
    #     mail.send(msg)

    #     return jsonify({'message': 'A new password has been sent to your email.'}), 200
    # else:
    #     return jsonify({'message': 'Failed to generate new password'}), 500
    otp = randint(000000,999999)
    email = "nanasih735@gmail.com"
    msg = Message(subject='OTP', sender ='anisahrab043@gmail.com', recipients = [email])
    msg.body = str(otp)
    mail.send(msg)
    return jsonify({'message': 'A new password has been sent to your email.'})
