def nan_expand(times):
    time = int(times)
    sum = ""
    if(time == 0):
        return ""
    else:
        count = 0
        while(count != time):
            sum = sum + "Not a "
            count = count + 1
            if(count == time - 1):
                sum = sum + "Not a Nan"
                count = count + 1

    return sum


a = input()
print(nan_expand(a))
