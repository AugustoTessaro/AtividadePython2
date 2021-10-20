from typing import Iterable


nome = input("Digite um nome: ")

for posicao in range (len(nome)+1):
    print(nome[:posicao])



