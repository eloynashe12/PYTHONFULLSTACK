#1;Cuenta regresiva
def cuentaregresiva(num):
    arreglo=[]
    for i in range (num, 0, -1):
        arreglo.append(i)
    return arreglo
print(cuentaregresiva(5))


#2;Imprimir y devolver
def Imprimir_devolver(lista):
    print(lista[0])
    return lista[1]
print(Imprimir_devolver([1,2]))


#3;longitud
def longitud(lista):
    return lista[0] + len(lista)
print (longitud([1,2,3,4,5]))

#4;Valores mayores que el segundo
def valores_mayores(lista):
    if len(lista) < 2:
        return False
    output = []
    for i in range(0,len(lista)):
        if lista[i] > lista[1]:
            output.append(lista[i])
    print(len(output))
    return output
print(valores_mayores([5,2,3,2,1,4]))
print(valores_mayores([3]))

#5 Longitud,ese valor
def longitud_ese_valor(valor,tamaño):
    output = []
    for i in range(0,tamaño):
        output.append(valor)
    return output
print(longitud_ese_valor(7,4))
print(longitud_ese_valor(2,6,))