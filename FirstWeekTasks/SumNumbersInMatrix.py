def sum_matrix(m):
    sum = 0
    for v in m:
        for p in v:
            if(p > "0" and p <="9"):
                sum += int(p)

    return sum


m = input()
print(sum_matrix(m))