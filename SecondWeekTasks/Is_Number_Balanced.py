def is_number_balanced(number):
    count = len(number)
    s1 = 0
    s2 = 0
    for index in range(int(len(number)/2)):
        s1 = s1 + int(number[index])
        s2 = s2 + int(number[count - index - 1])


    if(s1 == s2):
        return True
    else:
        return False





number = input()
print(is_number_balanced(number))