from time import time
from random import randint
# import matplotlib.pyplot as plt

def linear_search(L, e):
    found = False
    i = 0
    while i < len(L): 
        if e == L[i]:
            found = True
            break
        i += 1
    print("LinearSearch tuvo: ",i,"iteraciones")
    return found,i

valores = []
for N in range(1,250):
    L = []
    for _ in range(N):
        L.append(randint(0,N))
    print("Longitud de L:",len(L))
    e = randint(-10,N+10)
    # tic = time() 
    found,cont = linear_search(L,e)
    valores.append(cont)
    # toc = time()
    # print("tiempo de ejecución:",toc-tic,"seg.")

promedio = sum(valores)/len(valores)
print("Promedio iteraciones",promedio)

# plt.plot(range(1,250),valores)
# plt.xlabel("N")
# plt.ylabel("# Iter")
# plt.show()