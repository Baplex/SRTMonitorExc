import redis
import threading

semaforo = threading.Semaphore(1)

#Conexion a redis
def get_redis_connection():
    """Obtiene la conexión a Redis"""
    return redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

#Storage de datos
def guardar_dato(clave, valor):
    """Guarda un dato en Redis con control de concurrencia"""
    with semaforo:
        redis_client = get_redis_connection()
        redis_client.set(clave, valor)
        print(f"✅ Dato guardado en Redis: {clave} -> {valor}")

#Get de los datos
def obtener_dato(clave):
    """Obtiene un dato de Redis con control de concurrencia"""
    with semaforo:
        redis_client = get_redis_connection()
        return redis_client.get(clave)
