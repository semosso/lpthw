directions = ["north", "south", "east", "west", "up", "down", "right", "left", "back"]
verbs = []
stops = []
nouns = []
numbers = [] # maybe not needed or different
errors = [] # maybe not needed, will be ELSE in scan?

def scan(frase):

    words = frase.split()
    lista = []

    for i in words: # porcão, mas vamos tentar fazer funcionar melhor em breve
        if i in directions:
            tupla = ("direction", i)
            lista.append(tupla)

    for i in verbs:
        if i in directions:
            tupla = ("verb", i)
            lista.append(tupla)

    for i in stops:
        if i in directions:
            tupla = ("stop", i)
            lista.append(tupla)

    for i in nouns:
        if i in directions:
            tupla = ("noun", i)
            lista.append(tupla)

    for i in numbers:
        if i in directions:
            tupla = ("number", i)
            lista.append(tupla)

    return lista