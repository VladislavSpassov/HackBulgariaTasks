from Fractions import simplify_fraction

import math
import sys



def lcm(x, y):
    # or can import gcd from `math` in Python 3
    return x * y // math.gcd(x, y)
def collect_fractions(fractions):

    nom = 0
    denom = 0
    f = []

    for tu in fractions:
        f.append(simplify_fraction(tu))



    gc = 0
    for index in range(len(f) - 1):
        current = math.gcd(f[index][1],f[index+1][1])
        if(current > gc):
            gc = current 

    result = []


    lc = 0
    for index in range(len(f) - 1):
        current = lcm(f[index][1],f[index + 1][1])
        if(current > lc):
            lc = current 
        

    for tu in f:
        current = (tu[0]* (lc // tu[1]) , lc)
        result.append(current)


    nom = 0
    for tu in result:
        nom += tu[0]

    return (simplify_fraction((nom,lc)))

