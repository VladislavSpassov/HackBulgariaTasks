def get_largest_palindrome(n):

    count = 0
    maxPal = 0

    while count < n:
        if(IsPalindrome(count)):
            maxPal = count
        count = count + 1

    return maxPal


def IsPalindrome(num):
    nstr = str(num)
    count = len(nstr)

    for index in range(len(nstr)):
        if(nstr[index] != nstr[count - index - 1]):
            return False


    return True


print(get_largest_palindrome(99))
print(get_largest_palindrome(252))
print(get_largest_palindrome(994687))
print(get_largest_palindrome(1000000000))