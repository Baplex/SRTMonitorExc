import redis
import time
from redis_client import obtener_dato

#Set de condiciones de min y max respiraciones permitidas
MIN_RESP = 12
MAX_RESP = 18

#Funcion de coleccion de valores respiratorios y alarma
def monitorear():

    #Opening de la excepcion
    try:
        respiraciones = obtener_dato("respiraciones")

        if respiraciones is None:
            print("No hay datos de respiración disponibles.")
        else:
            try:
                respiraciones = int(respiraciones)
                estado = "Normal"

                if respiraciones < MIN_RESP:
                    estado = "RESPIRACIÓN BAJA!!"
                elif respiraciones > MAX_RESP:
                    estado = "RESPIRACIÓN ALTA!!"

                print(f"Respiraciones: {respiraciones} resp/min - {estado}")

            #Excepcion 1 // Excepcion recursiva
            except ValueError:
                print("Error: El valor de respiraciones no es un número válido.")
                
    #Excepcion 2 // de cuando no se puede conectar al redis
    except redis.exceptions.ConnectionError:
        print("Error: No se pudo conectar a Redis.")

    time.sleep(2)
    monitorear()  # Llamada recursiva

# First call a la funcion
monitorear()
