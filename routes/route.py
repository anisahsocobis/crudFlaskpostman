from flask import Blueprint, jsonify

test_bp = Blueprint('main', __name__)

@test_bp.route('/execute-code', methods=['GET'])
def execute_code():
    result = "Flask executed successfully"
    return jsonify({"message": result})
