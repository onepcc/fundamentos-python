x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.- Actualiza los valores en diccionarios y listas
#a.- Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x[1][0]=15
print(x)

#Con funcion
def cambia(arr):
    print(f"antes: {arr}")
    for i in range (len(arr)):
        for m in range(len(arr[i])):
            print(arr[i][m])
            if arr[i][m] == 10:
                arr[i][m] = 15
    print(f"despues: {arr}")

x = [ [5,2,3], [10,8,9] ] 
cambia(x)



#b.- Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
students[0]["last_name"]="Bryant"
print(students)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

def cambiapellido(lista):
    print(f" antes:{lista}")
    for i in range(len(lista)):
        if lista[i]["last_name"]=="Jordan":
            lista[i]["last_name"]="Bryant"
    return lista
change =cambiapellido(students)
print(f"despues {change}")

#c.- En el directorio sports_directory, cambia 'Messi' a 'Andres'
sports_directory["soccer"][0]="Andres"
print(sports_directory)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
def cambianombre(lista):
    print(f" antes:{lista}")
    for i in range(len(lista)):
        
        if lista["soccer"][i]=="Messi":
            lista["soccer"][i]="Andres"
    return lista
mesias =cambianombre(sports_directory)
print(f"despues {mesias}")

#d.- Camba el valor 20 en z a 30
z[0]["y"]=30
print(type(z),z)

#2.- Itera a través de una lista de diccionarios
#Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, 
# la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado. 
# Por ejemplo, dada la siguiente lista:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for x in students:
        print(f'first_name - {x["first_name"]}, last_name - {"last_name"}')
        print(x)
    # for x in students:
    #     for k,v in x.items():
    #         print(k,v,end=" , ",sep=" - ")
    #         print(f"{k}: - ")
iterateDictionary(students) 
# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#3.- Obtén valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)que, # dada una lista de diccionarios y un nombre de clave, 
# la función imprima el valor almacenado en esa clave para cada diccionario. 
# Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:
# Michael
# John
# Mark
# KB

# Y iterateDictionary2('last_name', students) debería generar:
# Jordan
# Rosales
# Guillen
# Tonel
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(clave,students):
    for x in students:
        print(x[clave])
iterateDictionary2 ('first_name', students) 
iterateDictionary2('last_name', students)

# 4.- Itera a través de un diccionario con valores de listas
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, imprima el nombre de cada clave junto con el tamaño
#  de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:
# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def some_dict(undict):
    c=0
    for item in undict:
        print(f"{len(undict[item])} {item.upper()}")
        
        for valor in undict[item]:
            print(valor)
        print("")
some_dict(dojo)
