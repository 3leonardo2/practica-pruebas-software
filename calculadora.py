def validar_numeros(*valores):
    for valor in valores:
        # bool es subclase de int en Python, por eso se excluye aparte
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError(f"Valor no válido: '{valor}'. Solo se permiten números")

def sumar (a,b):
    validar_numeros (a,b)
    return a + b

def dividir (a,b):
    validar_numeros (a,b)
    if b==0:
        raise ValueError ("No se puede dividir entre cero")
    return a / b

def restar(a, b):
    validar_numeros(a, b)
    return a - b

def multiplicar(a, b):
    validar_numeros(a, b)
    return a * b
