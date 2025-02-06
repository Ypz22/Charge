import redis
import time
import json
import requests
import os
import sys

# Agregar "Charge/" al sys.path para importar main.py correctamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import commonHashBreaker

# Configurar Redis y servidor Master
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
MASTER_URL = "http://127.0.0.1:3000"

WORKER_ID = f"worker-{os.getpid()}"  # Identificador único del worker

def get_task():
    """ Intenta robar una tarea desde el master """
    while True:
        try:
            response = requests.get(f"{MASTER_URL}/steal_task")
            if response.status_code == 200:
                task = response.json()
                print(f"🟢 [{WORKER_ID}] Tarea obtenida: {task}")  
                return task
            elif response.status_code == 204:
                print(f"🔴 [{WORKER_ID}] No hay tareas disponibles en este momento.")
            else:
                print(f"🔴 [{WORKER_ID}] Error en la solicitud de tarea. Código: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"🔴 [{WORKER_ID}] Error al robar tarea: {e}")
        
        print(f"⏳ [{WORKER_ID}] Esperando 2 segundos antes de volver a intentar...")
        time.sleep(2)  # Espera antes de volver a intentar

def report_execution_time(task_hash, exec_time):
    """ Reporta el tiempo de ejecución de la tarea al master """
    try:
        response = requests.post(f"{MASTER_URL}/report_time", json={
            "worker_id": WORKER_ID,
            "hash": task_hash,
            "execution_time": exec_time
        })
        if response.status_code == 200:
            print(f"✅ [{WORKER_ID}] Tiempo reportado correctamente: {exec_time} segundos")
        else:
            print(f"⚠️ [{WORKER_ID}] Error al reportar tiempo: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ [{WORKER_ID}] Error al enviar tiempo de ejecución: {e}")

def process_task():
    """ Bucle para procesar tareas robadas """
    while True:
        task = get_task()
        if task and "hash" in task:
            hash_value = task["hash"]
            hash_type = task["hash_type"]
            dictionary_path = task["dictionary"]
            
            print(f"⚡ [{WORKER_ID}] Procesando tarea: {hash_value}")
            start_time = time.perf_counter()
            commonHashBreaker(hash_value, hash_type, dictionary_path)
            exec_time = time.perf_counter() - start_time
            
            print(f"✅ [{WORKER_ID}] Tarea {hash_value} completada en {exec_time:.4f} segundos.")
            report_execution_time(hash_value, exec_time)
        else:
            print(f"⏳ [{WORKER_ID}] No hay tareas disponibles. Intentando de nuevo en 2 segundos...")
            time.sleep(2)  # Espera antes de volver a intentar

if __name__ == "__main__":
    print(f"🟡 [{WORKER_ID}] Worker iniciado y listo para robar trabajo.")
    process_task()
