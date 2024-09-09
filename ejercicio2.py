class persona:
    def __init__ (self, coso1, coso2):
        self.coso1=coso1; self.coso2=coso2
arreglo = []
def ingresar(eleccion):
    for n in range(eleccion):
         cosa1 = int(input("ingrese coso1: "))
         cosa2 = int(input("ingrese coso2: "))
         arreglo.append(persona(cosa1, cosa2))
def escupir(eleccion):
    for i in range(eleccion):
         print("\nPara el elemento ", i+1, " es:\n", "El coso1 es: ", arreglo[i].coso1, " y el coso2 es: ", arreglo[i].coso2)        
def promedioCoso1(eleccion):
    prom=0
    for i in range(eleccion):
        prom += arreglo[i].coso1
    prom=prom/eleccion
    return prom
    
eleccion = int(input("Ingrese cantidad: "))
ingresar(eleccion)
escupir(eleccion)
print("El promedio es: ", round(promedioCoso1(eleccion),2))
