from typing import Iterable

def soma(element1, element2, element3):
    return(element1 + element2 + element3)

arg1 = input("Primeiro numero: ")
arg2 = input("Segundo numero: ")
arg3 = input("Terceiro numero: ")    

arg1 = int(arg1)
arg2 = int(arg2)
arg3 = int(arg3)


print("Soma dos argumentos: " ,soma(arg1, arg2, arg3) )