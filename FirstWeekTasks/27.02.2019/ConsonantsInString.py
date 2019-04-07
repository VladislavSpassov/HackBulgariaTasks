def count_consonants(str):
    count = 0
    for v in str:
        if(v != 'a' or v != 'e' or v != 'i'or  v != 'o' or  v != 'u' or  v != 'y'):
            count = count + 1
        elif(v != 'A' or v != 'E' or v != 'I'or  v != 'O' or  v != 'U' or  v != 'Y'):
            count = count + 1
    return count

a = input()
print(count_consonants(a))