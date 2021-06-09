#1.- Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

def big(valores):
    original = valores
    arr =[]
    for x in original:
        if x > 0:
            arr.append("big")
        else:
            arr.append(x)
    return arr
c = big([-1,3,5,-5])
print(c)


#2.- Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos.
# (Tenga en cuenta que cero no se considera un número positivo).
# Ejemplo: count_positives([- 1, 1, 1,1 ]) cambia la lista original a [-1, 1, 1, 3] y la devuelve
# Ejemplo: count_positives([1, 6, -4, -2, -7, -2]) cambia la lista a [1, 6, -4, -2, -7, 2] y la devuelve
def countplus(val):
    l = val
    cuenta = 0
    for num in l:
        if num >0:
            cuenta +=1
    # print(cuenta)
    l[len(l)-1] = cuenta
    return l
resp = countplus([-1,1,1,1])
print(resp)



# 3.-  Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7
def suma(lista):
    l = lista
    suma = 0
    for num in lista:
        suma += num
    return suma
r = suma([1,2,3,4])
r1 = suma([6,3,-2])
print (f"la suma de los valores es: {r}")
print (f"la suma de los valores es: {r1}")



# 4.- Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
def promedio(lista):
    l = lista
    suma = 0
    for num in lista:
        suma += num
    return suma/len(l)
r = promedio([1,2,3,4])
r1 = promedio([6,3,-2])
print (f"El promedio de los valores es: {r}")
print (f"El promedio de los valores es: {r1}")

# 5.- Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0
def largo(lista):
    l = lista
    if len(l) == 0:
        print("ta vacio")
    return len(l)
r = largo([1,2,3,4])
r1 = largo([])
print (f"La longitud del array es: {r}")
print (f"La longitud del array es: {r1}")


# 6.- Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, 
# haga que la función devuelva False.
# Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False
def minimo(lista):
    l = lista
    if len(l) == 0:
        return False
    min = l[0]
    for val in l:
        if val <min:
            min = val
    return min
r = minimo([37,2,1,-9])
r1 = minimo([])
print (f"El valor minimo es: {r}")
print (f"El valor minimo es: {r1}")



# 7.- Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. 
# Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False
def maximo (lista):
    l = lista
    max = l[0]
    if len(l)==0:
        return False
    else:
        for x in l:
            if x > max:
                max = x
    return max
print(maximo([37,2,1,-9]))


# 8.- Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}
def final(final):
    l = final
    min= l[0]
    max= l[0]
    suma = 0
    promedio =0
    dicc ={}
    for valor in l:
        if valor < min:
            min = valor
        elif valor > max:
            max = valor
        suma += valor
        promedio = suma /len(l)
    dicc ={"total":suma,"promedio":promedio,"minimo":min,"maximo":max,"longitud":len(l)}
    return dicc

final = final([37,2,1,-9])
print(final)
#asi se accede a los valores de los diccionarios
print(final["minimo"])


# 9.- Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. 
# Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]
def inversa (lista):
    l = lista
    half= int((len(l))/2)
    for x in range(0,half,1):
        l[x],l[(len(l)-1)-x]=l[(len(l)-1)-x],l[x]
    return l
print(inversa([37,2,1,-9,10,8]))