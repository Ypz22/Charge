from flask import Flask, request, jsonify
import threading
import time
import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import main as hashBreaker

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_next_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

class Server:
    def __init__(self, name, task_function):
        self.name = name
        self.task_function = task_function

    def handle_request(self, hash_value):
        start_time = time.time()
        print(f"{self.name} está procesando la solicitud con hash {hash_value}...")
        self.task_function(hash_value)
        end_time = time.time()
        processing_time = end_time - start_time
        print(f"{self.name} procesó la solicitud con hash {hash_value} en {processing_time:.2f} segundos.")
        return processing_time

def task_server_1(hash_value):
    if hash_value:
        password = hashBreaker.commonHashBreaker(hash_value, "md5", "dic.txt")
        print(f"Servidor 1: Realizando operación con hash {hash_value}. Contraseña: {password}")

def task_server_2(hash_value):
    if hash_value:
        password = hashBreaker.commonHashBreaker(hash_value, "md5", "dic.txt")
        print(f"Servidor 2: Realizando operación con hash {hash_value}. Contraseña: {password}")

def task_server_3(hash_value):
    if hash_value:
        password = hashBreaker.commonHashBreaker(hash_value, "md5", "dic.txt")
        print(f"Servidor 3: Realizando operación con hash {hash_value}. Contraseña: {password}")

servers = [
    Server("Servidor 1", task_server_1),
    Server("Servidor 2", task_server_2),
    Server("Servidor 3", task_server_3)
]

load_balancer = LoadBalancer(servers)

def handle_request_thread(hash_value):
    next_server = load_balancer.get_next_server()
    print(f"Procesando la solicitud con hash {hash_value}...")
    processing_time = next_server.handle_request(hash_value)
    print(f"Tiempo total de procesamiento de la solicitud: {processing_time:.2f} segundos.")

@app.route('/api', methods=['GET'])
def api():
    hash_value = request.args.get('param')
    if hash_value:
        thread = threading.Thread(target=handle_request_thread, args=(hash_value,))
        thread.start()
        return jsonify({"message": "Solicitud en proceso"}), 202
    else:
        return jsonify({"error": "Falta el parámetro 'param'"}), 400

if __name__ == '__main__':
    app.run(port=3000)