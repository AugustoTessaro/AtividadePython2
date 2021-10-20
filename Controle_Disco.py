


with open('Usuarios.txt', 'r') as arquivo:
    for posicao, valores in (enumerate(arquivo)):
        print(posicao + 1, valores)
        
