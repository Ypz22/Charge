from flask import Flask, request, jsonify
import sys
import os

# Agregar la carpeta "Charge/" al sys.path para que Python encuentre main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import main as hashBreaker  # Ahora podrá importar "main.py"


app = Flask(__name__)

@app.route('/process', methods=['GET'])
def process_request():
    param = request.args.get('param', default='', type=str)
    
    if not param:
        return jsonify({'error': 'No parameter provided'}), 400

    # Procesa el hash con el diccionario
    output = hashBreaker.commonHashBreaker(param, "md5", "dic.txt")

    return jsonify({'worker': request.host, 'result': output})

@app.route('/', methods=['GET'])
def home():
    return "Nodo Trabajador - Esperando tareas"

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5001
    app.run(host='0.0.0.0', port=port, debug=True)
