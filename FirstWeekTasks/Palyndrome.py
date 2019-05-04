def palindrome(n):
    count = 0
    l = len(n) - 1
    while(count != round(len(n) / 2)):
        if(n[count] != n[l]):
            return False
        count = count + 1
        l = l - 1
    return True


n = input()
print(palindrome(n))