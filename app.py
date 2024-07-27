from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/execute-code', methods=['GET'])
def execute_code():
    # Place your code here
    result = "Flask executed successfully"
    return jsonify({"message": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
