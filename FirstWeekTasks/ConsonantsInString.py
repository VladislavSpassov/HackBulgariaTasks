def count_consonants(s):
    count = 0
    for v in s:
        if(v != 'a' and v != 'e' and v != 'i' and  v != 'o' and  v != 'u'and   v != 'y' and 
            v != 'A' and v != 'E' and v != 'I' and  v != 'O' and  v != 'U' and  v != 'Y'):
            count = count + 1
    return count

a = input()
print(count_consonants(a))
