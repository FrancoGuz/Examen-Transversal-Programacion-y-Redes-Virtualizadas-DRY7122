import geopy.distance
import unicodedata

# Definimos las coordenadas fuera de la función para que estén disponibles en todo el script
coordenadas = {
    'santiago': (-33.4489, -70.6693),
    'buenos aires': (-34.6037, -58.3816),
    'mendoza': (-32.8894, -68.8458),
    'valparaiso': (-33.0472, -71.6127)
    # Agrega más ciudades según sea necesario
}

def normalizar(texto):
    # Eliminar tildes y convertir a minúsculas
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8')
    return texto.lower()

def calcular_distancia(ciudad_origen, ciudad_destino):
    return geopy.distance.distance(coordenadas[ciudad_origen], coordenadas[ciudad_destino]).km

while True:
    print("Ingrese la ciudad de origen (o 's' para salir): ")
    origen = normalizar(input().strip())
    if origen == 's':
        break

    print("Ingrese la ciudad de destino: ")
    destino = normalizar(input().strip())

    if origen not in coordenadas or destino not in coordenadas:
        print("Ciudad no reconocida, intente nuevamente.")
        continue

    distancia_km = calcular_distancia(origen, destino)
    distancia_millas = distancia_km * 0.621371

    print(f"La distancia entre {origen} y {destino} es de {distancia_km:.2f} km o {distancia_millas:.2f} millas.")

    print("Ingrese el tipo de transporte (auto, avion, bicicleta): ")
    transporte = normalizar(input().strip())

    if transporte == "auto":
        duracion = distancia_km / 100  # supongamos 100 km/h
    elif transporte == "avion":
        duracion = distancia_km / 800  # supongamos 800 km/h
    elif transporte == "bicicleta":
        duracion = distancia_km / 20  # supongamos 20 km/h
    else:
        print("Tipo de transporte no reconocido.")
        continue

    print(f"La duración del viaje en {transporte} es de {duracion:.2f} horas.")
    print(f"De {origen} a {destino}, viajando en {transporte}, tomaría aproximadamente {duracion:.2f} horas.")
