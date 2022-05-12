from random import choice
def sorteia_pais(dic):
    países = []
    for país in dic.keys():
        países.append(país)
    sorteado = choice(países)
    return sorteado