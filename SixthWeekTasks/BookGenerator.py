import random 


def random_word_generator():
    with open("/etc/dictionaries-common/words","r") as f:
        index = 0
        s = ""
        lines = list(f)
        result = []
        while(index < 10):
            result.append(" ".join((random.sample(lines, 3))))
            index+=1
            
        return "\n".join(result)


    



print((random_word_generator()))