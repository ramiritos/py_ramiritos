

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