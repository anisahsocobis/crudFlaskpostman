from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from random import *

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'anIsah27$'
app.config['JWT_SECRET_KEY'] = 'anIsah27$'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'anisahrab043@gmail.com'
app.config['MAIL_PASSWORD'] = 'hasina28$'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
mail = Mail(app)
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=True)

    def __init__(self, email, password):
        self.email = email
        self.password = password

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    results = users_schema.dump(all_users)
    return jsonify(results)

@app.route('/users/<id>/', methods=['GET'])
def post_details(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

@app.route('/add_user', methods=['POST'])
def add_user():
    email = request.json['email']
    password = request.json['password']
    users = User(email, password)
    db.session.add(users)
    db.session.commit()
    return user_schema.jsonify(users)

@app.route('/update/<id>/', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    email = request.json['email']
    password = request.json['password']
    user.email = email
    user.password = password

    db.session.commit()
    return user_schema.jsonify(user)

@app.route('/delete/<id>/', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)

@app.route('/reset_password', methods=['POST'])
def reset_password():
    # if request.content_type != 'application/json':
    #     return jsonify({'message': 'Content-Type must be application/json'}), 400

    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if not user:
        return jsonify({'message': 'Email does not exist'}), 404

    new_password = 'temporary_password'
    user.password = generate_password_hash(new_password, method='sha256')
    db.session.commit()

    msg = Message('Password Reset Request',
                  sender='anisahrab043@gmail.com',
                  recipients=[user.email])
    msg.body = f'Your new temporary password is: {new_password}'
    mail.send(msg)

    return jsonify({'message': 'A new password has been sent to your email.'}), 200


@app.route("/api/legumes", methods=['GET'])
def get_legumes():
    return jsonify([
        {"id": 1, "name": "Carotte"},
        {"id": 2, "name": "Tomate"},
    ])

@app.route("/api/fruits", methods=['GET'])
def get_fruits():
    return jsonify([
        {"id": 1, "name": "Pomme"},
        {"id": 2, "name": "Banane"},
    ])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
