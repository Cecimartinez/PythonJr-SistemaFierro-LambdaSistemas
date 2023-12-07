def suma_de_digitos_potencia(n, potencia):
    return sum(int(digito) ** potencia for digito in str(n))

def es_numero_feliz(num, objetivo, potencia):
    numeros_vistos = set()
    while num != objetivo and num not in numeros_vistos:
        numeros_vistos.add(num)
        num = suma_de_digitos_potencia(num, potencia)
    return num == objetivo

def generar_numeros_felices(cantidad, objetivo=1, potencia=2):
    numeros_felices = []
    num = 1
    while len(numeros_felices) < cantidad:
        if es_numero_feliz(num, objetivo, potencia):
            numeros_felices.append(num)
        num += 1
    return numeros_felices

# Ejemplo de uso con variante opcional (a)
X = 10
valor_objetivo = 1
potencia_valor = 2
lista_numeros_felices = generar_numeros_felices(X, valor_objetivo, potencia_valor)
print(f"Los primeros {X} números felices con valor objetivo {valor_objetivo} y potencia {potencia_valor} son: {lista_numeros_felices}")
