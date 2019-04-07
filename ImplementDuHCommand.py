import os
import sys
def du(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size / 1000000000


def main():
    print(du(sys.argv[1])) 
    print("GB")


if(__name__ == "__main__"):
    main()

