def prime_factorization(n):
    p = int(n)
    l = {}
    while(p > 1):
        print(min_divider(p))
        if(min_divider(p) not in l.keys()):
            l[min_divider(p)] = 1
        else:
            l[min_divider(p)] = l[min_divider(p)] + 1 
        p = p / min_divider(p)

    for x in l.keys():
        print("({},{}), ".format(x,l[x]), end = " ")
        



def min_divider(n):
    p = int(n)
    for x in range(2,p):
        if(int(p % x) == 0):
            return x
        
    return p
    

a = input()
prime_factorization(a)
