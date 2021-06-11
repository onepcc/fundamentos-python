my_list = [99,4,2,5,-3]
my_tuple = (99,4,2,5,-3)
my_str = "sequoia"
print(my_list[:])
# salida: [99,4,2,5,-3]
print(my_tuple[1:])
# salida: (4,2,5,-3)
print(my_str[:3])
# salida: "seq"
print(my_tuple[2:4])
# salida: (2,5)
print(my_list, my_tuple, my_str)
# salida: [99,4,2,5,-3] (99,4,2,5,-3) 'sequoia' -- note fíjate que el valor original no cambió

# Algunos metodos
# max(sequence) devuelve el valor más grande en la secuencia
valores = [2,4,6,8,-4]
print(max(valores))
# sum(sequence) devuelve la suma de todos los valores en secuencia
valores = [2,4,6,8,-4]
print(sum(valores))
# map(function, sequence) aplica la función a cada elemento en la secuencia que pasa. Devuelve una lista de los resultados.
valores = [2,4,6,8,-4]
def duplica(x):
    x = x * 2
    return x
print(list(map(duplica,valores)))
# min(sequence) devuelve el valor más bajo en una secuencia.
valores = [2,4,6,8,-4]
print(min(valores))
# sorted(sequence) devuelve una lista ordenada de los valores de la secuencia
valores = [2,4,6,8,-4]
print(sorted(valores))


