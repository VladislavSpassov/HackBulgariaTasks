def chain(iter1,iter2):

    for x in iter1:
        yield x
    for x in iter2:
        yield x


print(list(chain(range(0,4),range(4,8))))


def compress(iterable,mask):
    index = 0
    for el in mask:
        print(el)
        if(el):
            index+=1
            yield iterable[index - 1]
        else:
            index+=1

print(list(compress(["Ivo", "Rado", "Panda","Ivan"], [False, False, True,True])))



def cycle(iterable):
    result = []
        
    while(True):
        lst = []
        for x in iterable:
            result.append(x)   

        
        yield result

endless = cycle(range(0,10)) 

for x in endless:
    print(x)

