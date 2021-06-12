arr = [8,7,5,1,3,10]

def bubble(arr):
    "Intercambia el valor de la der con la izq si es menor, compara con cada elemnto, luego de cada iteracion quedan ordenados el extremo derecho"
    for v in range(len(arr)-1):
        for x in range(len(arr)-1-v):
            if arr[x]>arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]
    return arr
                

print(bubble(arr))

