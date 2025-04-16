def cantidad_digitos(numero):
    if numero < 0:
        numero = -numero
    cadena = str(numero)
    return len(cadena)