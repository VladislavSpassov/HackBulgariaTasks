import sys

def SumIntgers(arguments):
    with open(arguments,'r') as f:
        s = 0
        line = f.readline()

        result = line.split(" ")
        result.remove("")
        r = map(int, result)
        print(sum(r))
        
        #result = int(f)
#        for l in line:
           
            
            
   
def main():

    SumIntgers(sys.argv[1])


if(__name__ == "__main__"):
    main()