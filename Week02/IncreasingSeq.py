def increasing_or_decreasing(seq):
    inc = True
    for index in range(1,len(seq)):
        if(seq[index] <= seq[index - 1]):
            inc = False

    dec = True
    for index in range(1,len(seq)):
        if(seq[index] >= seq[index - 1]):
            dec = False
        


    if(inc):
        print("Up!")
    elif(dec):
        print("Down!")
    else:
        print("False")


increasing_or_decreasing([1,2,3,4,5])
increasing_or_decreasing([5,6,-10])
increasing_or_decreasing([1,1,1,1])
increasing_or_decreasing([9,8,7,6])
