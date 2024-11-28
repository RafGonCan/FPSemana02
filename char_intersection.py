primeira = input()
segunda = input()

intersecao = set(primeira) and set(segunda)

conjunto = ""

for letras in primeira:
    if (letras in intersecao and letras not in conjunto):
        conjunto += letras

print(conjunto)


#intersecao = set(primeira).intersection(set(segunda))
#conjunto = "".join(intersecao)