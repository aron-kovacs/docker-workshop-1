from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)

CORS(app)


@app.route('/sayhello', methods=['GET'])
def say_hello():

    name = request.args.get('name')

    msg = "Hello"

    if name is not None:
        msg += " " + name

    return jsonify({
        "success": True,
        "message": msg
    })


@app.route('/readfile', methods=['GET'])
def read_file():

    msg = "The file content is: "

    with open('myfile', 'r') as the_file:
        msg += the_file.read().replace('\n', '')

    return jsonify({
        "success": True,
        "message": msg
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876)
