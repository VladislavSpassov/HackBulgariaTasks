import sys

from random import randint
print(randint(1, 1000))


def generate_numbers(filename, numbers):

    with open(filename,'r+') as f:
        for i in range(int(numbers)):
            p = randint(1,1000)
            f.write(str(p) + " ")



def main():
    generate_numbers(sys.argv[1],100)

if __name__ == '__main__':
    main()