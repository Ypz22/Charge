import redis
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configurar Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

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
    """ Permite que un worker robe una tarea de la cola """
    task_data = redis_client.lpop('task_queue')  # Roba la tarea más antigua
    if task_data:
        return jsonify(json.loads(task_data)), 200
    return jsonify({"error": "No hay tareas disponibles"}), 204

if __name__ == "__main__":
    print("Servidor Master ejecutándose en http://127.0.0.1:3000")
    app.run(host='127.0.0.1', port=3000, debug=True)
