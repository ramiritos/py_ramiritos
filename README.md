# py_ramiritos
trabajos de clase 

# ejemplo1 ingreso de datos naturales mcd
    
def calcular_mcd(a, b):#funcion para hallar el MCD
    while b:
        a, b = b, a % b
    return a

    # solicitud de datos
print("Cálculo del Máximo Común Divisor ")
num1 = int(input(("Ingrese el primer número: ")))
num2 = int(input(("Ingrese el segundo número: ")))

mcd = calcular_mcd(num1, num2)
print(f"El MCD de {num1} y {num2} es: {mcd}")


# ejemplo2 ingreso de ecepciones y condiciones para ingreso de datos correctos

def obtener_entero(mensaje):#para que pida constatemente el numero caso que se ingrese un numero no solicitado o no cumpla con el enunciado
    while True:
        try: #agregamos una excepcionasd
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("Por favor, ingrese un número mayor a cero")
        except ValueError:
            print("Error: Debe ingresar un número entero.")

def calcular_mcd(a, b):#funcion para hallar el MCD
    while b:
        a, b = b, a % b
    return a

    # solicitud de datos
print("Cálculo del Máximo Común Divisor dos números naturales.")
num1 = obtener_entero("Ingrese el primer número: ")
num2 = obtener_entero("Ingrese el segundo número: ")

mcd = calcular_mcd(num1, num2)
print(f"El MCD de {num1} y {num2} es: {mcd}")
