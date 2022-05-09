import math

class DemoException(Exception):
    def __init__(self, message):
        super().__init__(message)

message = "ValueError: fatorial() not defined for negative values."
message0 = "ValueError: raiz() not defined for negative values."
message1 = "TypeError: 'float' object cannot be interpreted as an integer."
message2 = "OverflowError: mat range error."

def emcima(numero):
    part = numero % 1
    if part == 0:
        if numero > 0:
            numero = int(numero)
            return numero
        else:
            numero = int(numero)
            return numero
    else:
        if numero > 0:
            numero = int(numero)
            return numero + 1
        else:
            numero = int(numero)
            return numero

def embaixo(numero):
    part = numero % 1
    if part == 0:
        if numero > 0:
            numero = int(numero)
            return numero
        else:
            numero = int(numero)
            return numero
    else:
        if numero > 0:
            numero = int(numero)
            return numero
        else:
            numero = int(numero)
            return numero - 1

def raiz(numero):
    j = 1
    cont = 0
    part = numero % 1
    if part == 0:
        if numero < 0:
            raise DemoException(message0)
        else:
            while numero != 0:
                numero = numero - j
                if numero < 0:
                    break
                else:
                    j = j + 2
                    cont = cont + 1
    else:
        raise DemoException(message1)
    return cont

def binario(numero):
    b = list()
    bina = ''
    j = 0
    while numero != 0:
        i = numero % 2
        i = str(i)
        b.append(i)
        j += 1
        numero = numero // 2
    j = j - 1
    while j >= 0:
        bina = bina + b[j]
        j -= 1
    return bina

def fatorial(numero):
    part = numero % 1
    fat = 1
    if part == 0:
        if numero > 100:
            raise DemoException(message2)
        elif numero <= 0:
            raise DemoException(message)
        else:
            while numero != 1:
                fat = fat * numero
                numero = numero - 1
    else:
        raise DemoException(message1)
    return fat

def potencia(base, exp):
    cont = 0
    pot = 1
    part = exp % 1
    if part == 0:
        if exp < 0:
            exp = exp * - 1
            base = 1 / base
            while cont != exp:
                pot = pot * base
                cont += 1
        else:
            while cont != exp:
                pot = pot * base
                cont += 1
    else:
        raise DemoException(message1)
    return pot

'''X = 9.785
print("FLOOR-> ", math.floor(X))
print("CEIL-> ", math.ceil(X))

print("EMBAIXO-> ", embaixo(X))
print("EMCIMA-> ", emcima(X))

print("POW-> ", math.pow(-3.1, -3))
print("Potência-> ", potencia(-3.1, -3))

print("Sqrt-> ", math.isqrt(14))
print("Raiz-> ", raiz(14))

print("Binario-> ", binario(5234))

print("Fatorial-> ", fatorial(8))
print("Fat-> ", math.factorial(8))'''