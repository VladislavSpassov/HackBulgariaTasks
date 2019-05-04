class Category:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return str("The name of the category is {0}".format(self.name))

    def __repr__(self):
        return self.__str__()

    def __eq__(self,other):
        return self.name == other.name



class Income(Category):
    def __init__(self,name,money):
        super().__init__(name)
        self.money = money
    def __str__(self):
        return str("{0},{1}".format(self.name,self.money))

    def __repr__(self):
        return [self.name,self.money]

    def __eq__(self,other):
        return self.name == other.name and self.money == other.money


class Expense(Category):
    def __init__(self,name,money):
        super().__init__(name)
        self.money = money
    def __str__(self):
        return str("{0},{1}".format(self.name,self.money))

    def __repr__(self):
        return [self.name,self.money]

    def __eq__(self,other):
        return self.name == other.name and self.money == other.money




