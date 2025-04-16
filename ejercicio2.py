
def cantidad_digitos_con_decimales(numero):
    aux = numero
    numero = abs(numero)
    cadena = str(numero)
    lista = cadena.split(".")
    #entero = int(lista[0])
    enteros = len(lista[0])
    decimales = lista[1]
    cont = 0
    for i in decimales:
        if i == "0":
            pass
        else:
            cont += 1
    if cont == 0:
        numero == int(numero)
        decimales = 0
    else:
        decimales = len(lista[1])

    return f"\nEl numero {aux} tiene:\nEnteros: {enteros}\nDecimales: {decimales}"

if __name__ == "__main__":
    numero = -0.0001
    resultado = cantidad_digitos_con_decimales(numero)
    print(resultado)