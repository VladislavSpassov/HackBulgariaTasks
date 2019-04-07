import sys
from .json2html import *

def Convert():
    j = {"name":"softvar","age":21}
    formatted_table = json2html.convert(json =j)
    print(formatted_table)





def main(file):
    Convert()
if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)

