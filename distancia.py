import geopy.distance

def calcular_distancia(ciudad_origen, ciudad_destino):
    coordenadas = {
        'Santiago': (-33.4489, -70.6693),
        'Buenos Aires': (-34.6037, -58.3816),
        'Mendoza': (-32.8894, -68.8458),
        'Valparaiso': (-33.0472, -71.6127)
        # Agrega más ciudades según sea necesario
    }
    return geopy.distance.distance(coordenadas[ciudad_origen], coordenadas[ciudad_destino]).km

while True:
    print("Ingrese la ciudad de origen (o 's' para salir): ")
    origen = input().strip()
    if origen.lower() == 's':
        break

    print("Ingrese la ciudad de destino: ")
    destino = input().strip()

    if origen not in coordenadas or destino not in coordenadas:
        print("Ciudad no reconocida, intente nuevamente.")
        continue

    distancia_km = calcular_distancia(origen, destino)
    distancia_millas = distancia_km * 0.621371

    print(f"La distancia entre {origen} y {destino} es de {distancia_km:.2f} km o {distancia_millas:.2f} millas.")

    print("Ingrese el tipo de transporte (auto, avión, bicicleta): ")
    transporte = input().strip().lower()

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

