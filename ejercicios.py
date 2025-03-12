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
 #HOLA MUNDO