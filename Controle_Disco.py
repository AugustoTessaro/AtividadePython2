from os import spawnl
import pandas as pd
import twilio as tw

usuarios = []
armaz_usuarios = []

tabela = pd.read_table('Usuarios.txt', header= None, sep=" ", names=["usuarios", "armazenamento_usuarios"])

#usuarios = 
#armaz_usuarios = tabela[1]

print(tabela["usuarios"])








print("ACME Inc. Uso do espaço em disco pelos usuário")
print("----------------------------------------------")
print("Nr. Usuário         Espaço         utilizado %")
