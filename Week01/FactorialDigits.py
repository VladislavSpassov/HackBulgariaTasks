def fact_digits(n):
    sum = 0
    p = int(n)
    while(p > 0):
        b = p % 10
        sum += fact(b)
        
        p //= 10
    return sum


def fact(n):
    p = int(n)
    if(p == 1 or p == 0):
        return 1
    else:
        return p * fact(p - 1)


a = input()
print(fact_digits(a))