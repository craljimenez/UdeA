from random import randint
from time import time

def binary_search(L, e):
    """
    L es una lista ordenada.
    """
    found = False
    lo = 0 # lower
    hi = len(L) - 1 # higher
    cont = 0
    while lo <= hi: 
        mid = (hi + lo) // 2 # Encontrando el valor medio entre lower y higher
        cont += 1
        if e > L[mid]:
            lo = mid + 1
        elif e < L[mid]:
            hi = mid - 1
        else:
            found = True
            break
    print("numero de iteraciones dadas:",cont)
    return found


L = []
for _ in range(10240):
    L.append(randint(-500,600))
print("Longitud de L:",len(L))
L.sort() # ordenando la lista
e = 456
tic = time() 
found = binary_search(L,e)
toc = time()
print("tiempo de ejecución:",toc-tic,"seg.")