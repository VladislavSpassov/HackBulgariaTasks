# cat2.py
import sys


def cat2(arguments):
    with open(arguments,'r') as f:
        data = f.read()
        print(data)

def main():
    for n in sys.argv[1:]:
        cat2(n)
        

if __name__ == '__main__':
    main()
