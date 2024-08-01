from flask import Flask
from flask_cors import CORS
from database import db
from database.legumes import legume_blueprint
from database.fruits import fruit_blueprint
from routes.route import test_bp
from routes.translation_route import translator_bp

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(legume_blueprint, url_prefix='/api')
app.register_blueprint(fruit_blueprint, url_prefix='/api')

app.register_blueprint(test_bp)
app.register_blueprint(translator_bp)

@app.before_request
def create_tables():
    db.create_all()
    # Vérifiez que les tables sont créées
    # print(db.engine.table_names())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
