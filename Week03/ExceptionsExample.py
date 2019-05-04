def SumInts(a,b):
    try :
        return 10/0

    except:
        raise ZeroDivisionError("cannot devidebyzero")

print(SumInts(4,1))
print(SumInts("ivan",5))

