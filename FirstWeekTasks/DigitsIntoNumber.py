def to_number(digits):
    ar =[]
    s = ""
    for v in digits:
        if(v >= "0" and v <= "9"):
            s = s + str(v)
    
    return s
    
    count = 0;
    #while(count != len(ar)):
     #   reversedAr[count] = 
    """while (di >= 0):
        print(ar)
        ar.append(di % 10)
        di //= 10
    return 0
"""
di =input()
print(to_number(di))