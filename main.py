def calcular_siguiente(serie):
    aux = serie[-1] + serie[-2]
    return aux

def funcion_bucle(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        serie = [0, 1]
        while len(serie) < n:
            siguiente_numero = calcular_siguiente(serie)
            serie.append(siguiente_numero)
        return serie

# Ejemplo de uso:
print(funcion_bucle(1000))