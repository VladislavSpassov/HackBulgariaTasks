import re



def sum_of_numbers(input_string):

    lst = (re.findall(r'\d+', input_string))
    return sum(map(int,lst))


print(sum_of_numbers("ab125cd3"))
print(sum_of_numbers("ab12"))
print(sum_of_numbers("ab"))
print(sum_of_numbers("1101"))
print(sum_of_numbers("1111O"))