#import pdb

#pdb.set_trace()
def is_credit_card_valid(number):
    num = str(number)
    lst = [int(i) for i in num]
    neuLst = []
    lst.reverse()
    for index,num in enumerate(lst):
        if(index % 2 == 1):
            lst[index] = lst[index] * 2

        neuLst.append(lst[index])

    print(sum(neuLst))

    s = 0
    for v in neuLst:
        print(v)
        if(v >=0 and v <= 9):
            s += v
            
        else:

            while(v > 9):

                add  = v % 10
                s+= add
                v //= 10

            s +=v

        print(s)

    if(s % 10 == 0):
        return True
    return False



print(is_credit_card_valid(79927398713))




