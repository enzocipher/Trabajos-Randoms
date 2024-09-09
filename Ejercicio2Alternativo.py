arreglo = {}
def GenerarPersonas(cantidad):
    for i in range(cantidad):
        arreglo["Persona"+str(i+1)]={}
    for i in range(cantidad):
        arreglo["Persona"+str(i+1)]["Edad"]=int(input("Ingrese edad: "))
        arreglo["Persona"+str(i+1)]["Nombre"]=str(input("Ingrese nombre: "))
def ImprimirGente(cantidad):
    print("Los nombres son: ")
    for i in range(cantidad):
        print(arreglo["Persona"+str(i+1)]["Nombre"])
def SumaEdad(cantidad):
    suma=0
    for i in range(cantidad):
        suma+=arreglo["Persona"+str(i+1)]["Edad"]
    print("El promedio es de: ", round((suma/cantidad),2))
cantidad=int(input("Ingrese cantidad de noobs: "))
GenerarPersonas(cantidad)
ImprimirGente(cantidad)
SumaEdad(cantidad)