def char_histogram(string):
    dict = {}

    for v in string:
        if(not(v in dict)):
            dict[v] = 1
        elif(v in dict):
            dict[v] = dict[v] + 1

    return dict

a = input()
print(char_histogram(a))