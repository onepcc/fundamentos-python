class Underscore:
    def map(self, iterable, callback):
        for x in range (len(iterable)):
            iterable[x]= callback(iterable[x])
        return iterable
   
    def find(self, iterable, callback):

        for x in iterable:
            if callback(x):
                return x
        return "HOLAfind"
    
    def filter(self, iterable, callback):
        lista2=[]
        for x in iterable:
            if (callback(x)):
                lista2.append(x)
        return lista2

    def filter2(self, iterable, callback):
        for x in iterable:
            if not(callback(x)):
                iterable.remove(x)
        return iterable
    
    def reject(self, iterable, callback):
        lista2=[]
        for x in iterable:
            if (callback(x)):
                lista2.append(x)
        return lista2

# has creado una libreria con 4 métodos
# se crea la instancia de la clse
_ = Underscore() # sí, estamos configurando una instancia a una variable que es un guión bajo
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)
# debe retornar [2, 4, 6] después que termines de implementar el código de arriba
print(_.map([1,2,3], lambda x: x*2)) # debe retornar [2,4,6]
print(_.find([1,8,3,4,5,6], lambda x: x>4)) # debe retornar el primer valor que es mayor que 4

print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # debe retornar [2,4,6]
print(_.filter2([1,2,3,4,5,6], lambda x: x%2==0)) # debe retornar [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2!=0)) # debe retornar [1,3,5]

def invoker(arr,callback):
    # invoque el input pasando 2 como argumento
    arr2 = []
    for x in arr:
        if (callback(x)):
            arr2.append(x)
    print(arr2)
invoker([1,2,3,4,5,6],lambda x: x%2==0)