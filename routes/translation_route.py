from flask import Blueprint, request, jsonify
from googletrans import Translator

translator_bp = Blueprint('translator', __name__)
translator = Translator()

@translator_bp.route('/translate')
def translate():
    text = request.args.get('text')
    target_lang = request.args.get('lang', 'fr')
    translation = translator.translate(text, dest=target_lang)
    return jsonify({'translated_text': translation.text})
