from flask import Flask, request, jsonify
import threading
import time
import random
import main as hashBreaker
from collections import deque

app = Flask(__name__)

class PredictiveLoadBalancer:
    def __init__(self, servers, history_size=5):
        self.servers = servers
        self.history = {server.name: deque(maxlen=history_size) for server in servers}

    def get_least_loaded_server(self):
        avg_loads = {server.name: (sum(self.history[server.name]) / len(self.history[server.name]) if self.history[server.name] else 0) for server in self.servers}
        best_server = min(self.servers, key=lambda server: avg_loads[server.name])
        return best_server
    
    def update_load(self, server_name, load_time):
        self.history[server_name].append(load_time)

class Server:
    def __init__(self, name, task_function):
        self.name = name
        self.task_function = task_function

    def handle_request(self, hash_value):
        start_time = time.time()
        print(f"{self.name} está procesando la solicitud con hash {hash_value}...")
        hashBreaker.commonHashBreaker(hash_value, 'md5', 'dic.txt')
        self.task_function(hash_value)
        end_time = time.time()
        processing_time = end_time - start_time
        print(f"{self.name} procesó la solicitud en {processing_time:.2f} segundos.")
        return processing_time

def task_server_1(hash_value):
    print("Servidor 1: Realizando operación")

def task_server_2(hash_value):
    print("Servidor 2: Realizando operación")

def task_server_3(hash_value):
    print("Servidor 3: Realizando operación")

servers = [
    Server("Servidor 1", task_server_1),
    Server("Servidor 2", task_server_2),
    Server("Servidor 3", task_server_3)
]

load_balancer = PredictiveLoadBalancer(servers)

def handle_request_thread(hash_value):
    best_server = load_balancer.get_least_loaded_server()
    print(f"Asignando solicitud con hash {hash_value} a {best_server.name}")
    processing_time = best_server.handle_request(hash_value)
    load_balancer.update_load(best_server.name, processing_time)

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