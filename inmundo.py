#Si el paciente dice que sí, el valor de a = 45.23
#Si el paciente dice que no, el valor de a = 56.22
def factorial(numero):
    resultado = 1
    while numero>0:
        resultado*= numero
        numero-=1
    return resultado


def decidirvalor():
    eleccion = 'd'
    while(True):
        eleccion = str(input("Tiene alguna bla bla bla y (si) / n (no)"))
        eleccion.upper()
        match eleccion:
            case 'Y': return 45.23; break;
            case 'N': return 56.22; break;

def formula(a, n):
    ResultadoFinal = 0
    for i in range(1, n+1):
        if (i%2 == 0):
            siesnegativo = -1
        else: siesnegativo = 1
        ResultadoFinal += siesnegativo*((a*i)/(factorial(i)))
        i+=1
    print("El resultado es: ", round(ResultadoFinal, 2))

if __name__ == "__main__":
    print("Bienvenido más capito")
    try: 
        n = int(input("Ingrese cantidad"))
    except ValueError:
        print("un solo trabajo tenias wn y pones algo q no es un numero")
    a = decidirvalor(); 
    print(a); print(factorial(3))
    formula(a, n)
