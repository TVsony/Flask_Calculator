from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Calculator"

@app.route('/cal', methods=["GET"])
def math_operation():
    data = request.json
    operation = data.get("operation")
    number1 = data.get("number1")
    number2 = data.get("number2")

    if operation not in ["add", "multiply", "division", "subtract"]:
        return jsonify({"success": False, "error": "Invalid operation"}), 400

    try:
        if operation == "add":
            result = int(number1) + int(number2)
        elif operation == "multiply":
            result = int(number1) * int(number2)
        elif operation == "division":
            if int(number2) == 0:
                return jsonify({"success": False, "error": "Division by zero"}), 400
            result = int(number1) / int(number2)
        else:
            result = int(number1) - int(number2)
        return jsonify({"success": True, "result": result}), 200
    except ValueError:
        return jsonify({"success": False, "error": "Invalid numbers"}), 400

if __name__ == '__main__':
    app.run(debug=True)

