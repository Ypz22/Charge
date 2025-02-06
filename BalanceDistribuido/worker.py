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

def get_task():
    """ Intenta robar una tarea desde el master """
    while True:
        try:
            response = requests.get(f"{MASTER_URL}/steal_task")
            if response.status_code == 200:
                task = response.json()
                print(f"🟢 Tarea obtenida: {task}")  # Debug
                return task
            elif response.status_code == 204:
                print("🔴 No hay tareas disponibles en este momento.")
            else:
                print(f"🔴 Error en la solicitud de tarea. Código: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"🔴 Error al robar tarea: {e}")
        
        print("⏳ Esperando 2 segundos antes de volver a intentar...")
        time.sleep(2)  # Espera antes de volver a intentar

def process_task():
    """ Bucle para procesar tareas robadas """
    while True:
        task = get_task()
        if task and "hash" in task:
            hash_value = task["hash"]
            hash_type = task["hash_type"]
            dictionary_path = task["dictionary"]
            
            print(f"⚡ Procesando tarea: {hash_value}")
            commonHashBreaker(hash_value, hash_type, dictionary_path)
            
            print(f"✅ Tarea {hash_value} completada. Buscando otra...")  # Debug
        else:
            print("⏳ No hay tareas disponibles. Intentando de nuevo en 2 segundos...")
            time.sleep(2)  # Espera antes de volver a intentar

if __name__ == "__main__":
    print("🟡 Worker iniciado y listo para robar trabajo.")
    process_task()
