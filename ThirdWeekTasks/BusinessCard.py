import sys
import json
def Convert(filename):
    f = open(filename,'r')
    json_data = json.load(f)
    f.close()
    new_file = open("newfile.txt","w+")
    for k,people in json_data.items():
        for person in people:
            new_file.write('<!DOCTYPE html>\n<html>\n<head>\n\t<title>'+person['first_name']+' '+person['last_name']+'</title>')
            new_file.write('\n')

            new_file.write('\t<link rel="stylesheet" type="text/css" href="styles.css">')   
            new_file.write('\n')    
            new_file.write('</head>')
            new_file.write('\n')
            new_file.write('<body>')
            new_file.write('\n')

            new_file.write('\n\t<div class="business-card' + " " +  person["gender"] + ">")
            new_file.write("\n\t<h1 class=full-name>" +person['first_name']+' ' + person['last_name']+'</h1>')
                



def main():
    Convert("data1.json")

if __name__ == '__main__':
    #filename = sys.argv[1]
    main()

