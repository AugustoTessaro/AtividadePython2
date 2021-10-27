from os import spawnl
import pandas as pd
import twilio as tw

usuarios = []
armaz_usuarios = []

tabela = pd.read_table('Usuarios.txt', header= None, sep=" ")

usuarios = tabela[0]
armaz_usuarios = tabela[1]

print(usuarios,)

print(armaz_usuarios)






