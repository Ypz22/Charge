from flask import Flask, request, jsonify
import requests
import itertools

app = Flask(__name__)

# Lista de nodos trabajadores 
workers = ["http://127.0.0.1:5001", "http://127.0.0.1:5002", "http://127.0.0.1:5003"]

# Iterador para balanceo Round-Robin
worker_cycle = itertools.cycle(workers)

@app.route('/api', methods=['GET'])
def balance_request():
    param = request.args.get('param', default='', type=str)
    
    if not param:
        return jsonify({'error': 'No parameter provided'}), 400

    # Selecciona un trabajador de manera Round-Robin
    worker_url = next(worker_cycle)

    try:
        # Redirige la petición al nodo trabajador
        response = requests.get(f"{worker_url}/process?param={param}")
        return response.json()
    except Exception as e:
        return jsonify({'error': f'Worker {worker_url} is unavailable: {e}'}), 500

@app.route('/', methods=['GET'])
def home():
    return "Nodo Maestro - Balanceo centralizado activo"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
