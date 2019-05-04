def simplify_fraction(fraction):
   
    if not isinstance(fraction,tuple):
        raise ValueError("not a tuple")
    if(fraction[1] == 0):
        raise ZeroDivisionError('Division by 0')
    result = ()
    m = min(fraction[0],fraction[1])
    denominator = 0
    nominator = 0
    for n in range(m + 1):

        if(fraction[0] == 0):
            return (0,fraction[1])
        if(n == 0):
            continue
        if(n > fraction[0] or n > fraction[1]):
            break
        if(fraction[0] % n == 0 and fraction[1] % n == 0):
            nominator = fraction[0] // n
            denominator = fraction[1] // n

    result = (nominator,denominator)
    return result

#print(simplify_fraction((4,4)))
#simplify_fraction((4,0))
#print(simplify_fraction((3,9)))

#print(simplify_fraction((1,7)))

#print(simplify_fraction((4,10)))

#print(simplify_fraction((63,462)))

#print(simplify_fraction((0,5)))

#print(simplify_fraction((1,2)))
#print(simplify_fraction((4,0)))