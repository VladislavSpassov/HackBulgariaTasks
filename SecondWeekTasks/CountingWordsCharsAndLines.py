import sys
import os
import re
import pdb


def Count(command, file):
    if(command == "chars"):
        with open(file,'r') as f:
            s = 0 
            for line  in f:
                current = line.split()
                for c in current:
                    for ch in c:
                        s +=1

            return s
                
    elif(command == "words"):
        with open(file,'r') as f:
            s = 0
            for line in f:
                current = line.split()
                for c in current:
                    if(len(c) == 0 or len(c) == 1):
                        continue
                    s +=1
                    print(c)
                    

            return s

    elif(command == "lines"):
        with open(file,'r') as f:
            s = 0
            for line in f:
                print(line)
                
                s+=1

            return s

    else:
        print("Not valid command")
        return 0


print(Count(sys.argv[1],sys.argv[2]))

