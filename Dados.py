import random
from typing import Iterable

lista_valores = []

for i in range(0,100):
    lista_valores.append(random.randint(1,6))

lista_valores = list(map(str,lista_valores))

print(' - '.join(map(str,lista_valores)))
    
lista_valores = list(map(int,lista_valores))

contador1 = lista_valores.count(1)
print("O numeor 1 se repetiu:" , contador1)

contador1 = lista_valores.count(2)
print("O numeor 2 se repetiu:" , contador1)

contador1 = lista_valores.count(3)
print("O numeor 3 se repetiu:" , contador1)

contador1 = lista_valores.count(4)
print("O numeor 4 se repetiu:" , contador1)

contador1 = lista_valores.count(5)
print("O numeor 5 se repetiu:" , contador1)

contador1 = lista_valores.count(6)
print("O numeor 6 se repetiu:" , contador1)


