from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Setup logging to console
logging.basicConfig(
    level=logging.INFO,  # Log level
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]  # Log to console
)

@app.route('/')
def home():
    app.logger.info('Home route accessed')
    return "Simple Calculator API"

@app.route('/calculate', methods=['GET'])
def calculate():
    try:
        # Get query parameters
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        operation = request.args.get('operation')

        app.logger.info(f"Received calculation request: {operation} {num1}, {num2}")
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                app.logger.error('Division by zero error')
                return jsonify(error="Cannot divide by zero"), 400
            result = num1 / num2
        else:
            app.logger.error(f"Invalid operation: {operation}")
            return jsonify(error="Invalid operation"), 400
        
        app.logger.info(f"Calculation result: {result}")
        return jsonify(result=result)

    except Exception as e:
        app.logger.error(f"Error during calculation: {str(e)}")
        return jsonify(error="Invalid input or operation"), 400

if __name__ == '__main__':
    app.run(debug=True)
