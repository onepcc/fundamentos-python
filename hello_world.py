# 1. TAREA: imprimir "Hola mundo"
print("Hola Mundo" )

# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Juan Pablo"
print( "Hola",name)	# con una coma
print( "Hola" + name )	# con un + 

# 3. imprimir "Hola 42!" con un numero en una variable
name = 20
print( "Hola", name )	# con una coma
print( "Hola " + str(name)+ " !")	# Solucion
print("Hola " + name + "!") #Error

# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "shawarma"
fave_food2 = "helado"

print("Me encanta comer " + fave_food1 + " and " + fave_food2 +".")

print("Me encanta comer {} and {}.".format(fave_food1,fave_food2)) # con .format()

print( f"Me encanta comer {fave_food1} and {fave_food2}." ) # con una cadena f