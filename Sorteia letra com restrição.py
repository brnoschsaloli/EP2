import random as r
def sorteia_letra(palavra,lista):
    especiais =['.', ',', '-', ';', ' ']
    x = r.choice(palavra)
    y = 0
    mai = [z.upper() for z in lista]
    minu = [w.lower() for w in lista]
    for e in palavra:
        if e not in especiais and e not in lista and e not in mai and e not in minu:
            y = 1
    if y == 0:
        return ''

    while x in especiais or x in lista or x in mai or x in minu:
        x = r.choice(palavra)
        
    return x