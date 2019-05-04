def max_consequtive(lis):
    b = [int(x) for x in lis if x >= "0" and x <= "9"]
    print(b)
    maxcount = []
    index = 0
    while index < len(b):
        maxcount.append(currentCount(index,b))
        index = index + currentCount(index,b)

    return max(maxcount)

def currentCount(index,l):
    current = []
    current.append(l[index])
    index = index + 1
    count = 1
    while(index < len(l)):
        if(l[index] in current):
            count = count + 1
        else:
            break
        index = index + 1


    return count

a = input()
print(max_consequtive(a))