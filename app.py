from flask import Flask
from routes.route import test_bp
# from translation_routes import translator_bp

app = Flask(__name__)

app.register_blueprint(test_bp)
# app.register_blueprint(translator_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
