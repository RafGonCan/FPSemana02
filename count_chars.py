frase = input()
frase_lista = frase.split()
palavras_frase = {}

for palavra in frase_lista:
    if (palavra in frase_lista):
        palavras_frase[palavra] = len(palavra)

print(palavras_frase)