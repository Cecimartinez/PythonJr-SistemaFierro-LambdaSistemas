import csv
from collections import defaultdict
from datetime import datetime

def es_en_la_manana(hora):
    # verifica si la hora  está en la mañana, en el rango de 6 a 11:59 hs.
    return 6 <= hora.hour < 12

def leer_archivo_csv(ruta_archivo):
    # lectura del archivo CSV 
    with open(ruta_archivo, newline='', encoding='utf-8') as csvfile:
        lector_csv = csv.DictReader(csvfile)
        for fila in lector_csv:
            yield fila

def analizar_recorridos_bicicletas(ruta_archivo):
    # analiza el archivo de recorridos de bicicletas y devuelve las tres estaciones de origen más activas durante la mañana 
    estaciones_activas = defaultdict(int)

    for fila in leer_archivo_csv(ruta_archivo):
        try:
            tiempo_str = fila['fecha_origen_recorrido']
            tiempo = datetime.strptime(tiempo_str, '%Y-%m-%d %H:%M:%S')

            if es_en_la_manana(tiempo):
                id_estacion_origen = fila['id_estacion_origen']
                nombre_estacion_origen = fila['nombre_estacion_origen']
                estaciones_activas[(id_estacion_origen, nombre_estacion_origen)] += 1
        except ValueError as e:
            # manejo de errores al convertir fechas
            print(f"Error al convertir la fecha en la fila: {fila}")
            print(f"Mensaje de error: {e}")

    estaciones_top = sorted(estaciones_activas.items(), key=lambda x: x[1], reverse=True)[:3]
    return estaciones_top

if __name__ == "__main__":
    ruta_archivo_recorridos = "./Bici-estaciones/trips_2023.csv"

    try:
        resultado = analizar_recorridos_bicicletas(ruta_archivo_recorridos)

        print("Las tres estaciones de origen más activas en la mañana son:")
        for (id_estacion, nombre), recorridos in resultado:
            print(f"Estación ID: {id_estacion}, Estación: {nombre}, Recorridos: {recorridos}")

    except FileNotFoundError:
        # manejo de error si no se encuentra el archivo
        print(f"No se pudo encontrar el archivo '{ruta_archivo_recorridos}'. Verifica la ubicación del archivo.")
    except ValueError as e:
        # manejo de errores al analizar el archivo CSV
        print(f"Se produjo un error al analizar el archivo: {e}")
    except Exception as e:
        # menejo de otros errores inesperados
        print(f"Se produjo un error inesperado: {e}")
