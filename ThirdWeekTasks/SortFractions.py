
def Division(tuple):
    x,y = tuple
    return float(x / y)


def sort_fractions(fractions):
    return sorted(fractions,key = Division)

print(sort_fractions([(1,4),(3,4),(1,2)]))




