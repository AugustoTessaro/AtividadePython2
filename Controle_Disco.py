from os import spawnl
import pandas as pd
import twilio as tw

'''
with open('Usuarios.txt', 'r') as arquivo:
    for posicao, valores in (enumerate(arquivo)):
        print(posicao + 1, valores)
'''

usuarios = []
armaz_usuarios = []

tabela = pd.read_table('Usuarios.txt', header= None, sep=" ")

usuarios = tabela[0]
armaz_usuarios = tabela[1]

print(usuarios,armaz_usuarios)








