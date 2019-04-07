def sum_of_digits(n):
    sum = 0
    p = int(n)
    while p != 0:
 
        
        sum +=( p % 10)
        p /= 10
    return round(sum) - 1


a = input()

print(sum_of_digits(a))


def sum_of_digits1(n):
    g = int(n)
    p = abs(g)

    digits = [(int)ch for ch in(n)]

    return sum(digits)


a = input()
print(sum_of_digits1(a))
