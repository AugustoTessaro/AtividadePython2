from typing import Iterable
import statistics
import sys


nome_atleta = input("Atleta: ")
if nome_atleta == '':
    sys.exit()


saltos_atleta = []

for posicao in range(0,5):
    
    saltos_atleta.append(input("Salto: "))



print('Atleta: ', nome_atleta )

print( ' - '.join(map(str,saltos_atleta)))

saltos_atleta = list(map(float, saltos_atleta))

media = (sum(saltos_atleta)/len(saltos_atleta))
print("Resultado Final: " , media, "m")


  

    



