from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def hello_word():
    return "hello world!"


@app.route('/manicures', methods=['GET'])
def get_manicures():
    return jsonify({'error': 'method unimplemented' })


@app.route('/manicures/<int:manicure_id>', methods=['GET'])
def get_manicure(manicure_id):
    return jsonify({'error': 'method unimplemented' })


@app.route('/manicures', methods=['POST'])
def create_manicure():
    return jsonify({'error': 'method unimplemented' })


@app.route('/manicures', methods=['PUT'])
def update_manicure():
    return jsonify({'error': 'method unimplemented' })


@app.route('/manicures', methods=['DELETE'])
def delete_manicure():
    return jsonify({'error': 'method unimplemented' })


if __name__ == '__main__':
    app.run()

