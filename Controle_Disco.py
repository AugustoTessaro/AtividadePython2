from os import spawnl
import pandas as pd
import twilio as tw

def convert_byte_megabyte(numero_byte):
    numero_Kbyte = numero_byte/1024
    numero_Mbyte = round((numero_Kbyte/1024),2)
    return numero_Mbyte

def calcula_porcent(espaco_total, espaco_util):
    espaco_porcent = round((espaco_util/espaco_total)*100,2)
    return espaco_porcent



tabela = pd.read_table('Usuarios.txt', header= None, sep=" ", names=["usuarios", "armazenamento_usuarios"])

espaco_total = tabela["armazenamento_usuarios"].sum()






