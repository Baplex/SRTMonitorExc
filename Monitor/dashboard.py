import redis
import time
import matplotlib.pyplot as plt
#Conexion a redis
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

valores = []
tiempos = []

#Creacion del graph
plt.ion() 
fig, ax = plt.subplots()
ax.set_ylim(5, 25)
ax.set_xlabel("Tiempo")
ax.set_ylabel("Respiraciones por minuto")

#Funcion generadora de valores en el graph
while True:
    respiraciones = redis_client.get("respiraciones")
    #ponemos los valores de respiracion en los valores de x, y respectivamente
    if respiraciones:
        respiraciones = int(respiraciones)
        valores.append(respiraciones)
        tiempos.append(len(valores))

        if len(valores) > 50:
            valores.pop(0)
            tiempos.pop(0)
        #Generacion de las lineas de la graph y los otros elementos
        ax.clear()
        ax.plot(tiempos, valores, marker="o", linestyle="-", color="b")
        ax.set_ylim(5, 25)
        ax.set_xlabel("Tiempo")
        ax.set_ylabel("Respiraciones por minuto")
        ax.set_title("Monitoreo de Respiración en Tiempo Real")
        plt.pause(1)

    time.sleep(1)
