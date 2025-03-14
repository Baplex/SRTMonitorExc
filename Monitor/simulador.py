from redis_client import guardar_dato
import time
import random
import redis


# Funcion para generar Respiraciones por min
def simular():
    #Opening del excepcion
    try:
        respiraciones = random.randint(8, 22)  # Genera un valor aleatorio
        guardar_dato("respiraciones", respiraciones) 

        print(f"Respiración registrada: {respiraciones} resp/min")
    #Excepcion 1 // no se conecta al redis
    except redis.exceptions.ConnectionError:
        print("Error: No se pudo conectar a Redis.")

    time.sleep(2)  # Espera antes de la siguiente llamada
    simular()  # Llamada recursiva en lugar de while True

# First call
simular()
