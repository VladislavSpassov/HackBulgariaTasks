def count_vowels(string):
    count = 0
    for v in string:
        if(v == 'a' or v == 'e' or v == 'i'or  v == 'o' or  v == 'u' or  v == 'y'):
            count = count + 1
        if(v == 'A' or v == 'E' or v == 'I'or  v == 'O' or  v == 'U' or  v == 'Y'):
            count = count + 1
    return count

a = input()
print(count_vowels(a))