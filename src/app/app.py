from flask import Flask, jsonify, request
app = Flask(__name__)

# Hello World output
@app.route('/')
def hello():
    return "Hello World!"

# A route that takes a name as a parameter and outputs a greeting
@app.route('/hello/<name>')
def hello_name(name):
    return f"Hallo, {name}!"

# A JSON-Route for data output
@app.route('/data')
def data():
    return jsonify({'key': 'value', 'int': 1})

# A POST-Route that takes JSON-data and returns it
@app.route('/post', methods=['POST'])
def post_data():
    data = request.json
    return jsonify(data), 201
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')