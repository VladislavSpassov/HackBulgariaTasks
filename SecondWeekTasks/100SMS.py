import pdb


def separate_list_into_string(lst):
    result = []
    current = ""
    for index in range(len(lst) - 1):
        current += str(lst[index])
        if(lst[index] != lst[index + 1]):
            result.append(current)
            current = ""

        if(index == len(lst) - 2):
            result.append(current + str(lst[len(lst) - 1]))

    return result

def numbers_to_message(pressed_sequence):
    d = {"2":["a","b","c"],
         "3":["d","e","f"],
         "4":["g","h","i"],
         "5":["j","k","l"],
         "6":["m","n","o"],
         "7":["p","q","r","s"],
         "8":["t","u","v"],
         "9":["w","x","y","z"]
         }
  
    lst = separate_list_into_string(pressed_sequence)
    
    message = ""
    up = False
    for index in range(len(lst)):

        if(lst[index] == "-1"):
            message+=""
            continue
        if(lst[index] == "1"):
            up = True
            continue
        if(lst[index] == "0"):
            message+=" "
            continue
        letter = d[lst[index][0]][(len(lst[index]) - 1 ) % len(d[lst[index][0]])]
        if(up == True):
            message+=letter.upper()
            up = False
            continue
        message += letter    
        
    print(message)

numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2])
#pdb.set_trace()

numbers_to_message([2, 2, 2, 2])

numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2])

