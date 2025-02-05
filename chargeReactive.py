from flask import Flask, request, jsonify
import main as hashBreaker
import requests
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

app = Flask(__name__)

def process_hash(param):
    """Función auxiliar para ejecutar la tarea en paralelo."""
    return hashBreaker.commonHashBreaker(param, "md5", "dic.txt")

@app.route('/api', methods=['GET'])
def get_data():
    param = request.args.get('param', default='', type=str)
    
    if not param:
        return jsonify({'error': 'No parameter provided'}), 400
    
    with ProcessPoolExecutor() as executor:
        future = executor.submit(process_hash, param)
        output = future.result()
    
    return jsonify({'message': f'Result: {output}'})

@app.route('/', methods=['GET'])
def home():
    return "Hello, this is a parallel Python server!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
