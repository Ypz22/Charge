from flask import Flask, request, jsonify
import main as hashBreaker

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    param = request.args.get('param', default='', type=str)
    if not param:
        return jsonify({'error': 'No parameter provided'}), 400
    hashBreaker.commonHashBreaker(param, "md5", "dic.txt")
    return jsonify({'message': f'Received: {param}'})


@app.route('/', methods=['GET'])
def home():
    return "Hello, this is a simple Python server!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)