from math import sin
from math import cos
from math import asin
from math import radians
def haversine(r,sig1,lamb1,sig2,lamb2):
    sig1 = radians(sig1)
    sig2 = radians(sig2)
    lamb1 = radians(lamb1)
    lamb2 = radians(lamb2)
    diam = 2*r
    lambs = (sin((lamb2 - lamb1)/2))**2
    sigs = (sin((sig2 - sig1)/2))**2
    coss = cos(sig1)*cos(sig2)
    raiz = ((sigs) + (coss)*(lambs))**(0.5)
    d = 2*r*(asin(raiz))
    return d