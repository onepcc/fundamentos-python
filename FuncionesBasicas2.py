# 1.- Cuenta regresiva : crea una función que acepte un número como entrada. 
# Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
# Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]
def regresivo(n):
    arr = []
    for x in range(n,-1,-1):
        arr.append(x)
    return arr
print(regresivo(6))

def regresivo2(n):
    arr = []
    for x in range(0,n+1,1):
        arr.append(x)
    arr.reverse()
    return arr
print(regresivo2(6))


# 2.- Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
# Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2
def imprime2(lista):
    arr = lista
    print(arr[0], "impreso")
    return arr[1]

print(f"{imprime2([1,2])}", end=" retornado")



# 3.- First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
# Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)
def onemaslargo(a,b,c,d,e):
    l = [a,b,c,d,e]
    return int(l[0])+len(l)

print(onemaslargo(1,2,3,4,5))

def maslargo(lista):
    lista1 = lista
    return int(lista1[0])+len(lista1)

print(maslargo([1,2,3,4,5]))

def listacarga(n):
    carga =[]
    for x in range (0,int(n),1):
        carga.append(int(input("Ingrese un numero: ")))

    return (carga,int(carga[0])+len(carga))
n=input("Ingrese n de elementos de la lista: ")
r=listacarga(n)
print(f"LISTA",     "SUMA")
print(r)



# 4.- Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de 
# la lista original que sean mayores que su segundo valor. 
# Imprima cuántos valores son y luego devuelva la nueva lista. 
# Si la lista tiene menos de 2 elementos, haga que la función devuelva False
# Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
# Ejemplo: values_greater_than_second ([3]) debería devolver False

def listamayor(n):
    "Toma una lista y devuleve el numero de elementos que son mayores a su segundo elemento, devuelve una lista nueva con esos elementos"
    temp = n
    otra =[]
    c=0
    if len(temp)<2:
        return False

    for x in temp:
        if x > temp[1]:
            c+=1
            otra.append(x)
    print(f"Mayores al 2 elemento: {c}")
    return otra
retorno = (listamayor([5,2,3,2,1,4]))
print(f"La lista devuelta es : {retorno}")
            



    

# 5.- Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
# La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
# Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
# Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]
def tamañovalor(a,b):
    "Ingresa tamaño y valor, devuelve una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados "
    lista =[]
    for x in range(0,a,1):
        lista.append(b)
    return lista
print(tamañovalor(4,7))
print(tamañovalor(6,2))

