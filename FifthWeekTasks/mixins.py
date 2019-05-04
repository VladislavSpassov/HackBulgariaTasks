import json 

class Jsonable:
    def to_json(self,indent=4):
        result = {}
        result["dict"] = {}
        for key,value in self.__dict__.items():
            result["dict"][key] = value

        

        currentType = str(self.__class__).split('.')[1].split("'")[0]
        #print(currentType)

        result["type"] = currentType
        
        
        return result


    @classmethod
    def from_json(cls,json_string): 
        obj = cls()
        for key,value in json_string["dict"].items():
            setattr(obj,key,value)
        return obj




class Xmlable:
    def to_xml(self):
        result = []
        currentType = str(self.__class__).split('.')[1].split("'")[0]

        current = "<" + currentType + ">"   #"</" + str(typ) + ">" 
            #to make it only Panda without the additional text

            
        for key,value in self.__dict__.items():
            current = "<" + currentType + ">"   #"</" + str(typ) + ">" 
        
            c = "<" + str(key) + ">" + str(value) + "</" + str(key) + ">" 
            for index in range(len(current)):
                if(current[index] == ">" ):
                    current = current + c
                    #print(current)
                    break

            current = current + "</" + str(currentType) + ">" 
            result.append(current)

        res = ""
        for v in result:
            res+= v
            res+=" "
        print(res)
        return res
            

    @classmethod
    def from_xml(cls,xml_string):
        obj = cls()
        result = []

        lst = xml_string.split()

        #print(xml_string)
        for el in lst:
            
            sub = str(el[7:len(el) - 8])

            #print(sub)
            c = 0
            for index in range(len(el)):
                if(sub[index] == ">"):
                    break

                c+=1

            #print(c)
            attr = sub[1:c]
            #print(attr)
            start = sub.find('>')
            end = sub.rfind('<')
            val = sub[start + 1:end]
            setattr(obj,attr,val)
        return obj

class Panda(Jsonable,Xmlable):
    def __init__(self,name="",age = 3):
        self.name = name
        self.age = age
   

    def __eq__(self,other):
        return self.name == other.name and int(self.age) == int(other.age)
    def __str__(self):
        return str("{0}-{1}".format(self.name,self.age))
p = Panda(name='Ivo',age = 15)
json_string = p.to_json()
xml_string = (p.to_xml())
print(xml_string)
#print(json_string)
p1 = Panda.from_json(json_string)
p2 = Panda.from_xml(xml_string)

#print(p,p2)
assert p == p1
assert p == p2
assert p1 == p2
