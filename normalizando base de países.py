def normaliza(dicio):
    países = {}
    for país in dicio.values():
        for p,info in país.items():
            países[p] = info
    return países