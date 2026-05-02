from aircraft import Aircraf
modelo = input("Enter aircraft model:\n")
plane = Aircraf(modelo)
while True:
    comando = input("Enter command (A for ascent, D for descent, X to exit):\n")
    if comando == 'X':
        break
    partes= comando.split()
    accion = partes[0]
    pies = int(partes[1])
    if accion == 'A':
        plane.climb(pies)
    elif accion == 'D':
        plane.descend(pies)
print(plane.altitude)