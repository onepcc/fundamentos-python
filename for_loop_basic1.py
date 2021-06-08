# Crea un archivo de Python llamado for_loop_basic1.py que realice las siguientes tareas.

# 1.-Básico : imprime todos los enteros del 0 al 150.
for i in range (1,151):
    print ("numero:",i)


# 2.-Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for i in range (5,1005,5):
    print ("numero:",i)

# 3.- Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".
for i in range (1,101):
    if i%10==0:
        print ("numero:",i ,"Coding Dojo 10")
    elif i%5 ==0:
        print ("numero:",i,"Coding 5")
        

#4.- Suma enteros impares de 0 a 500,000 e imprime la suma final.
sum=0
for n in range(1,50,2):
    if n%2!=0:
        sum+=n
print("impar ",n,sum)

#5.- Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
for i in range(2018,-1,-4):
    print(i)


#6.- Contador flexible : establece tres variables: lowNum, highNum, mult. 
#Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult.
#Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
def contador(lowNum,HighNum,mult):
###Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult.
    for i in range (lowNum,HighNum+1):
        if i % mult==0:
            print(i)
contador(2,9,3)

# 7.- BONUS: ¿Cómo se puede detectar si un número es primo? 
#     Es divisible por el mismo y por 1
# ¿Cómo retornar una lista con los primos entre el 1 y el 1000?

def es_primo(numero):
    """Verifica si un numero es primo, divide el numero ingresado entre el 2 hasta el mismo numero-1
    .Si es divisible entre 1 y el mismo numero, es primo"""
    resultado = True
    for divisor in range (2, numero):
        if(numero%divisor) == 0:
            resultado = False
            break
    return resultado

es = es_primo(7)
print (es)

lista =[]
for i in range (1,100):
    if es_primo(i):
        lista.append(i)
        print(lista)
    


#Retos de Profesor
#- Crear una función que recorra cada valor de la lista e imprima cada valor
lista = ['pedro','juan','diego']

def recorre (lista):
    for val in lista:
        print(f" valor : {val}")
    for count, val in enumerate(lista):
        print(count,val)
recorre(lista)


#- Crea una función que toma una lista como argumento y devuelve una suma de todos sus valores
def recorresuma(asumar):
    suma = 0
    for x in asumar:
        suma += x
    return suma
numeros =[1,2,3,4,5,6,7,8,9]

print(recorresuma(numeros))

# GRUPO 2: 

# Crea una funcion que dado una palabra diga si es palindroma o no.
# slice(start, stop, step)
# string[start:end:step]

def palindromo(word):
    if word == word[::-1]:
        print ("Es palindromo")
    else:
        print("no es palindromo")

palindromo("juan")


# OTRO: 
# - Crea una función que tome una lista y devuelva el primer y el último valor de la lista. 
# Si la longitud de la lista es menor que 2, haga que devuelva False.

def lista(valor):
    if len(valor) < 2:
        print("pocos argumentos")
        return False
    recorte = [valor[0], valor[len(valor)-1]]
    print(recorte)
    print(f"El primer valor es {valor[0]} y el ultimo es {valor[-1]}")
    return recorte

valor = [11,22,35,4]
otro = lista (valor)
print(otro)

# - Crea una función que tome una lista y devuelva un diccionario con su mínimo, máximo, promedio y suma
def dictnuevo(lista):
    dict={}
    minimo = min(lista)
    maximo = max(lista)
    suma = sum (lista)
    promedio = suma/(len(lista))

    dict= {"minimo":minimo,"maximo":maximo,"suma":suma,"promedio":promedio}
    print(dict)

l= [1,2,3,4,5,6]
dictnuevo(l)




#Print time 
from datetime import datetime
def printTime(tarea):
    
    print(f"{tarea} terminada el {datetime.now()}")

printTime("prueba")

reverso = [1,2,3,4]

def rev(lista):
    lista.reverse()
    print(lista)
    return lista

print(reverso)
rev(reverso)
print(reverso)