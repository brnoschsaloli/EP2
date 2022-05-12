def esta_na_lista(pais,lista):
    x = 0
    for e in lista:
        if pais in e[0]:
            x = 1
    if x == 1:
        return True
    
    if x == 0:
        return False