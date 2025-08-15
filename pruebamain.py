from prueba3.prueba3 import ClaseDos
import os

ruta = os.path.join("prueba3","palabras.txt")
waw = ClaseDos(str(input("dame un nombre: ")))
print(waw.nombre)

if input("quieres escribir y/n") == "y":
    lineas = int(input("lineas a escribir: ?"))
else:
    lineas = 0

with open(ruta,"a") as f:
    for i in range(lineas):
        f.write(input()+"\n")

ruta = os.path.join("prueba3","oracion.txt")

with open(ruta,"r") as leer:
    lineas = leer.readlines()
lineas = "".join(lineas)
lineas = lineas.split(",")
lineas = " ".join(lineas)
print(lineas)

