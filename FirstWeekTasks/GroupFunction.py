

def group_function(items):
    b = [int(i) for i in items if i >= "0" and i <= "9"]
    result = []
    index = 0

    while index < len(b):
        result.append(sequence(index,b))
        print(result)
        index = index + len(sequence(index,b))
        print(index)
    return result


def sequence(ind,b):
    current = []
    current.append(b[ind])
    ind = ind + 1
    
    while(ind< len(b) - 1):
        
        if(b[ind] not in current):
            break
        
        elif(b[ind] in current):
            current.append(b[ind])
        ind = ind + 1
        print(current)
        
    return current 


a = input()
print(group_function(a))