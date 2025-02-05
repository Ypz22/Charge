from flask import Flask, request, jsonify
import main as hashBreaker
import concurrent.futures
import queue

app = Flask(__name__)
executor = concurrent.futures.ThreadPoolExecutor()
task_queue = queue.Queue()

# Balanceo de carga reactivo
def process_request():
    while True:
        param = task_queue.get()
        if param is None:
            break
        hashBreaker.commonHashBreaker(param, "md5", "dic.txt")
        task_queue.task_done()

@app.route('/api', methods=['GET'])
def get_data():
    param = request.args.get('param', default='', type=str)
    if not param:
        return jsonify({'error': 'No parameter provided'}), 400
    
    task_queue.put(param)
    return jsonify({'message': f'Processing: {param}'})

@app.route('/', methods=['GET'])
def home():
    return "Hello, this is a simple Python server!"

if __name__ == '__main__':
    for _ in range(4):  # Se crean 4 trabajadores para procesar solicitudes
        executor.submit(process_request)
    
    app.run(host='0.0.0.0', port=3000, debug=True, threaded=True)