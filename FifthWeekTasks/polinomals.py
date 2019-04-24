class Polynom:
    lst = []
    lstSigns = []
    derivatives = []
    @classmethod
    def convert_string_to_many_mononoms(cls,s):
        withoutSpaces = s.split(" ")
        mons = []
        for sign in withoutSpaces:
            if(sign == "+" or sign == "-"):
                Polynom.lstSigns.append(sign)


        for mon in withoutSpaces:
            if(mon != "+" and mon != "-"):
                mons.append(mon)

        for mon in mons:
            if("^" not in mon):
                if("x" not in mon):
                    degree = 0
                else:
                    degree = 1
            else:
                degree = (mon[len(mon) - 1:len(mon)])
            if(mon[0] == "x"):
                coef = 1
            else:
                coef = mon[0]

            obj = Mononom(coef,degree)
            Polynom.lst.append(obj)
        
    @classmethod
    def calcMonoms(cls):
        final = ""
        count = 0
        for obj in Polynom.lst:
            if(obj.degree == 1):
                newObj = Mononom(obj.coef)
                Polynom.derivatives.append(newObj)
            elif(obj.degree == 0):
                Polynom.lstSigns.remove(Polynom.lstSigns[count - 1])
                
            else:

                newObj = Mononom(int(obj.coef) * int(obj.degree),int(obj.degree) - 1)
                Polynom.derivatives.append(newObj)

            count+=1

    @classmethod
    def build_string_of_derivatives(cls,s):
        cls.convert_string_to_many_mononoms(s)
        cls.calcMonoms()
        signs = [x for x in s if(x == "+" or x == "-")]
        print(signs)
        count = 0
        fin = ""
        for der in cls.derivatives:
            
            if(count == 0):
                count = 1
                fin = fin  + str(der)
                continue

            fin += Polynom.lstSigns[count - 1] + str(der)


        return fin

class Mononom:
    def __init__(self,coef = 1,degree = 0):
        self.coef = coef
        self.degree = degree

    def __str__(self):
        if(self.degree == 1):
            if(self.coef != 0):
                return str("{0}x".format(self.coef))

        if(self.degree == 0):
            return self.coef
        return str("{0}x^{1}".format(self.coef,self.degree))
    def __repr__(self):
        return  self.__str__()


def main():
    print(Polynom.build_string_of_derivatives("2x^2 + 5"))
if(__name__ == "__main__"):
    main()
