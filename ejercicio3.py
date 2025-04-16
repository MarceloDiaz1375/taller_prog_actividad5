
def num_compuesto_lista(lista):
    compuestos = []
    for numero in lista:
        cont = 1
        divisores = 0
        while cont <= numero:
            if numero%cont == 0:
                divisores += 1
            cont += 1
        if divisores > 2:
            compuestos.append(numero)
        #    print("numero compuesto")
        #elif divisores == 2:
        #    print("numero primo")
        #else:
        #    print("el numero es 1")
    return compuestos

if __name__ == "__main__":
    numeros = [1, 2, 3, 10, 11, 8, 17, 35]
    resultado = num_compuesto_lista(numeros)
    print(resultado)