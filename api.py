import pdb
from flask import Flask, jsonify, make_response, abort, request

app = Flask(__name__)
manicures = [
        {
            'id': 1,
            'polishes': [{'brand': 'essie', 'name': 'mint candy apple', 'colors': ['#A4D9D0']}],
            'photo': '/static/1.jpg',
            'name': 'Slightly Chipped Mint Candy Apple',
        },
        {
            'id': 2,
            'polishes': [
                    {'brand': 'deborah lippmann', 'name': 'when lightning strikes', 'colors': ['#FFFFFF', '#999EA0']},
                    {'brand': 'opi', 'name': 'give me the moon', 'colors': ['#cfc7dd']},
            ],
            'photo': '/static/2.jpg',
            'name': 'Moon Lightning'
        }
    ]

@app.route('/')
def hello_word():
    return "hello world!"


@app.route('/manicures', methods=['GET'])
def get_manicures():
    return jsonify({ 'manicures': manicures })


@app.route('/manicures/<int:manicure_id>', methods=['GET'])
def get_manicure(manicure_id):
    for m in manicures:
        if m['id'] == manicure_id:
            return jsonify({ 'manicure': m })
    abort(404)


@app.route('/manicures', methods=['POST'])
def create_manicure():
    #pdb.set_trace()
    if not request.json or not 'name' in request.json:
        abort(400)
    manicure = {
                'id': manicures[-1]['id'] + 1,
                'name': request.json['name'],
                'polishes': request.json.get('polishes', []),
                'photo': request.json.get('photo', '')
                }
    manicures.append(manicure)
    print manicures
    return jsonify({'manicure': manicure}), 201


@app.route('/manicures/<int:manicure_id>', methods=['PUT'])
def update_manicure(manicure_id):
    for m in manicures:
        if m['id'] == manicure_id:
            m['name'] = request.json.get('name', m['name'])
            m['polishes'] = request.json.get('polishes', m['polishes'])
            m['photo'] = request.json.get('photo', m['photo'])
            return jsonify({ 'manicure': m })

    abort(400)


@app.route('/manicures/<int:manicure_id>', methods=['DELETE'])
def delete_manicure(manicure_id):
    for m in manicures:
        if m['id'] == manicure_id:
            manicures.remove(m)
            return jsonify({ 'result': 'deleted' })

    abort(400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)

