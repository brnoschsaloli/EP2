def adiciona_em_ordem(pais,distancia,lista):
    nova_lista = [pais,distancia]
    copia = []
    if pais in lista:
        return lista
    x = 0
    i = 0
    while i < len(lista):
        if nova_lista[1] < lista[i][1] and x == 0:
            copia.append(nova_lista)
            x = 1
        else:
            copia.append(lista[i])
            i += 1
    if x == 0:
        copia.append(nova_lista)
    return copia
    
