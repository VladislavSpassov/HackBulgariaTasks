import json     
import sys


def CodingSkills(file):

    with open(file) as json_file:
        data =json.load(json_file)
        result = {}
        for p in data["people"]:
            for s in p["skills"]:
                if(s["name"] not in result):
                    result[s["name"]] = 0

        for p in data["people"]:
            for s in p["skills"]:
                for key,value in result.items():
                    
                    if(s["name"] == key and s["level"] > value):
                        result[key] = s["level"]

        
        for key,value in result.items():
            for p  in data["people"]:
                for s in p["skills"]:
                    if(key ==  s["name"] and value == s["level"]):
                        print(s["name"],p["first_name"],p["last_name"])
                        break


    







def main():
    CodingSkills(sys.argv[1])


if(__name__ == "__main__"):
    main()