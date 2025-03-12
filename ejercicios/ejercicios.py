## Crea una función que reciba un número entero y devuelva la suma de todos sus dígitos
def sumarDigitos(numero):
 # La suma inicialmente es 0
    suma = 0
 # Convertimos en cadena el número
    numero = str(numero)
 # Para cada cifra de las existentes
    for i in numero:
 # Sumamos la variable convirtiendo el valor de cadena a entero
        suma += int(i)
 # Devolvemos la suma
    return suma
 # PROGRAMA
print(sumarDigitos(323))
        
## Escribe una función que reciba un número y genera su tabla de multiplicar hasta el 10, mostrando los resultados
## en formato de lista.

def tabla(numero):
    if numero == 1:
        resultado = [numero * 1, numero * 2, numero * 3, numero * 4, numero * 5, numero * 6, numero * 7, numero * 8, numero * 9, numero * 10]
    elif numero == 2:
        resultado = [numero * 1, numero * 2, numero * 3, numero * 4, numero * 5, numero * 6, numero * 7, numero * 8, numero * 9, numero * 10]
    elif numero == 3:
        resultado = [numero * 1, numero * 2, numero * 3, numero * 4, numero * 5, numero * 6, numero * 7, numero * 8, numero * 9, numero * 10]
    elif numero == 4:
        resultado = [numero * 1, numero * 2, numero * 3, numero * 4, numero * 5, numero * 6, numero * 7, numero * 8, numero * 9, numero * 10]
    elif numero == 5:
        resultado = [numero * 1, numero * 2, numero * 3, numero * 4, numero * 5, numero * 6, numero * 7, numero * 8, numero * 9, numero * 10]
    elif numero == 6:
        resultado = [numero * 1, numero * 2, numero * 3, numero * 4, numero * 5, numero * 6, numero * 7, numero * 8, numero * 9, numero * 10]
    elif numero == 7:
        resultado = [numero * 1, numero * 2, numero * 3, numero * 4, numero * 5, numero * 6, numero * 7, numero * 8, numero * 9, numero * 10]
    elif numero == 8:
        resultado = [numero * 1, numero * 2, numero * 3, numero * 4, numero * 5, numero * 6, numero * 7, numero * 8, numero * 9, numero * 10]
    elif numero == 9:
        resultado = [numero * 1, numero * 2, numero * 3, numero * 4, numero * 5, numero * 6, numero * 7, numero * 8, numero * 9, numero * 10]
    else:
        return "Número fuera de rango, por favor ingresa un número entre 1 y 9."

    return resultado  # Devolvemos la tabla de multiplicar

# Llamada a la función
print(tabla(1))  # Esto devolverá la tabla del 1

##  Escribe una función que recibe una lista de números y devuelva el promedio de los mismos

def promedio (lista):
    contador = 0
    for i in lista:
            contador+= i
    return contador/len(lista)

print(promedio([2, 3, 3]))

## Define una función que reciba una cadena de texto y cuente cuántas vocales (a, e, i, o, u) contiene

def vocales (lista):
    contador = 0
    for i in lista:
        contador+=1
    return contador
print(vocales(['a','e','i','o','u']))

# Lista invertida de numeros
def invertidos(numeros):
    return numeros[::-1]
        
        
print(invertidos([1,2,3,4]))

## Crea una función que reciba una lista de números y devuelva el valor máximo y mínimo de la lista.

def maxMin(numeros):
    if len(numeros) == 0:
        return None
    max = numeros[0]
    min = numeros [0]
    for i in numeros:
        if i > max:
            max = i
        if i < min:
            min= i
    return {"Minimo": min,"Máximo": max}
        
print(maxMin([2,3,4,5]))
