import codecs
from os import spawnl
from numpy import string_
import pandas as pd
from pandas.core.indexes.base import Index
import twilio as tw

def convert_byte_megabyte(numero_byte):
    numero_Kbyte = numero_byte/1024
    numero_Mbyte = round((numero_Kbyte/1024),2)
    return numero_Mbyte

def calcula_porcent(espaco_total, espaco_util):
    espaco_porcent = round((espaco_util/espaco_total)*100,2)
    return espaco_porcent

tabela = pd.read_table('Usuarios.txt', header= None, sep=" ", names=["Usuario","Espaço Utilizado"])

espaco_total = tabela["Espaço Utilizado"].sum()

tabela["% do uso"] = calcula_porcent(espaco_total,tabela["Espaço Utilizado"])
tabela["Espaço Utilizado"] = convert_byte_megabyte(tabela["Espaço Utilizado"])

tabela["Espaço Utilizado"] = tabela["Espaço Utilizado"].astype("string")
tabela["% do uso"] = tabela["% do uso"].astype("string")

for i in tabela.index:
    tabela.at[i,"Espaço Utilizado"] = f'{tabela.at[i,"Espaço Utilizado"]} MB'
    tabela.at[i,"% do uso"] = f'{tabela.at[i,"% do uso"]} %'
    
tabela.insert(loc=0,column="Nr.",value=range(1,7))

numero_linha,numero_coluna = tabela.shape
espaco_medio = espaco_total/numero_linha

espaco_medio = convert_byte_megabyte(espaco_medio)
espaco_total = convert_byte_megabyte(espaco_total)

w = codecs.open("Relatorio.txt","w","utf-8")

w.write(tabela.to_string(index=False))
w.write(f"\nEspaço Total: {espaco_total} MB\n")
w.write(f"Espaço Médio: {espaco_medio} MB")
w.close()








