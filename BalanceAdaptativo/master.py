import redis
import time
import json
import sys
import os
from flask import Flask, request, jsonify

# Agregar la carpeta "Charge/" al sys.path para importar main.py correctamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import commonHashBreaker

app = Flask(__name__)

# Conectarse a Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Diccionario para almacenar tiempos promedio de cada worker
worker_times = {}

@app.route('/add_task', methods=['POST'])
def add_task():
    """ Agrega una nueva tarea a la cola """
    data = request.json
    if "hash" in data and "hash_type" in data and "dictionary" in data:
        redis_client.rpush('task_queue', json.dumps(data))
        return jsonify({"message": "Tarea agregada correctamente"}), 200
    return jsonify({"error": "Datos inválidos"}), 400

@app.route('/steal_task', methods=['GET'])
def steal_task():
    """ Permite que un worker robe una tarea de la cola y equilibra la carga según el tiempo promedio """
    task_data = redis_client.lpop('task_queue')  # Roba la tarea más antigua

    if task_data:
        task = json.loads(task_data)

        # Asignar worker en base a su desempeño (balanceo adaptativo)
        if worker_times:
            best_worker = min(worker_times, key=worker_times.get)  # El worker más rápido
            print(f"🟢 Asignando tarea {task['hash']} al worker más rápido: {best_worker}")

        return jsonify(task), 200
    return jsonify({"error": "No hay tareas disponibles"}), 204

@app.route('/report_time', methods=['POST'])
def report_time():
    """ Recibe tiempos de ejecución de workers y los almacena en Redis """
    data = request.json
    worker_id = data.get("worker_id")
    task_hash = data.get("hash")
    execution_time = data.get("execution_time")

    if worker_id and task_hash and execution_time is not None:
        if worker_id not in worker_times:
            worker_times[worker_id] = []  # Inicializar como lista

        worker_times[worker_id].append(execution_time)

        # Calculamos el tiempo promedio sin sobrescribir la lista
        avg_time = sum(worker_times[worker_id]) / len(worker_times[worker_id])

        print(f"📊 [{worker_id}] Tiempo promedio actualizado: {avg_time:.4f} segundos")

        return jsonify({"message": "Tiempo registrado", "average_time": avg_time}), 200

    return jsonify({"error": "Datos inválidos"}), 400


if __name__ == "__main__":
    print("🚀 Servidor Master ejecutándose en http://127.0.0.1:3000")
    app.run(host='127.0.0.1', port=3000, debug=True)
