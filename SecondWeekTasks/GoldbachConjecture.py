def goldbach(n):
    result = []
    current = ()

    for x in range(2,n):
        if(IsPrime(x)):
            current = (x,)
            for p in range(2,n // 2 + 1):
                if(IsPrime(p) and x + p == n):
                    tup = current + (p,)
                    result.append(tup)

    print(result)



def IsPrime(n):
    for x in range(2,n):
        if(n % x == 0):
            return False


    return True

goldbach(4)
goldbach(6)
goldbach(8)
goldbach(10)
goldbach(100)
