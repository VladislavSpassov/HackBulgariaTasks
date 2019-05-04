

class Bill:
    def __init__(self,amount):
        if(type(amount) is not int):
            raise TypeError

        if(amount < 0):
            raise ValueError

        self.amount = amount
        self.count = 0
    def __str__(self):
        return("A {0}$ bill".format(self.amount))
    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount
    def __eq__(self,other):
        if(self.amount == other.amount):
            return True

        return False
    def  __hash__(self):
        
        return hash(self.amount)



class BatchBill:
    def __init__ (self, lst):
        for el in lst:
            if(not isinstance(el,Bill)):
                raise TypeError

        self.lst = lst
    def __len__(self):
        count = 0
        for el in self.lst:
            count +=1

        return count
    def total(self):
        s = 0
        for el in self.lst:
            s += int(el)

        return s

    def __getitem__(self, index):
        return self.lst[index]


class CashDesk:

    def __init__(self):
        self.current = []


    def total(self):
        return self.current


    def append(item):
        self.current.append[item]
    def take_money(self,money):
        if(not isinstance(money,Bill)  and  not isinstance(money,BatchBill)):
            raise TypeError
        if(isinstance(money,Bill)):
            self.current.append(money.amount)
            print(self.current)
        else:
            for el in money:
                self.current.append(el.amount) 



    def inspect(self):
        
        d = {}
        for el in [Bill(value) for value in self.current]:
            if(str(el) not in d):

                d[str(el)] = 1
            else:
                d[str(el)] += 1
        print(d)
def main():
    a = Bill(10)
    b = Bill(5)
    c = Bill(10)
    print(int(a),int(b),int(c))
    print(str(a))
    print(a)
    print(a==b)
    print(a==c)
    money_holder = {}
    money_holder[a] = 1
    if(c in money_holder):
        money_holder[c] +=1

    print(money_holder)


    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BatchBill(bills)
    for bill in batch:
        print(bill)


    desk = CashDesk()
    desk.take_money(batch)
    desk.take_money(Bill(10))
    desk.inspect()
    print(desk.total())
if(__name__ == "__main__"):
    main()
