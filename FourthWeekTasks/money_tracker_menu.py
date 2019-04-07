from aggregated_money_tracker import ConvertToDict
from category import *



class Menu:
    d = ConvertToDict.create_dict("money_tracker.txt")
    @staticmethod
    def list_user_data(date = ""):
        
        if(date != ""):
            if(date in Menu.d.keys()):
                print(Menu.d[date])
            else:
                print("no such date ")
        print(Menu.d)
        for key in Menu.d:
            print(key)
            for lst in Menu.d[key]:
                print(lst)

    @staticmethod
    def generate_all_user_incomes(file_name):
        
        incomes = []
        for key in Menu.d:
            for lst in Menu.d[key]:

                current = []
                if(lst[2] == " New Income"):
                    income = Income(lst[1],lst[0])
                    current.append(lst[1])
                    current.append(lst[0])
                    incomes.append(income)
        

        return incomes
     
    @staticmethod
    def generate_all_user_expenses(file_name):
        expenses = []
        for key in Menu.d:
            for lst in Menu.d[key]:

                current = []
                if(lst[2] == " New Expense"):
                    expense = Expense(lst[1],lst[0])
                    current.append(lst[1])
                    current.append(lst[0])
                    expenses.append(expense)

        return expenses

    @staticmethod
    def show_user_incomes(all_user_data):
        lst = Menu.generate_all_user_incomes(all_user_data)
        for el in lst:
            print(el.name,el.money)

    @staticmethod
    def show_user_savings(all_user_data):
        d = Menu.generate_all_user_incomes(all_user_data)
        savings = []
        for income in d:
            if(income.name == " Savings"):
                savings.append(income)

        for s in savings:
            print(s)
    @staticmethod
    def show_user_deposits(all_user_data):
        incomes = Menu.generate_all_user_incomes(all_user_data)
        deposits = []
        for inc in incomes:
            if(inc.name == " Deposit"):
                print(inc)

    @staticmethod
    def show_user_expenses(all_user_data):
        result = Menu.generate_all_user_expenses(all_user_data)
        for el in result:
            print(el.name,el.money)

    @staticmethod
    def list_income_categories(all_user_data):
        result = Menu.generate_all_user_incomes(all_user_data)
        lst = []
        for x in result:
            if(x.name not in lst):
                lst.append(x.name)
                print(x.name)

    @staticmethod
    def list_expense_categories(all_user_data):
        result = Menu.generate_all_user_expenses(all_user_data)
        lst = []
        for x in result:
            if(x.name not in lst):
                lst.append(x.name)
                print(x.name)

    @staticmethod
    def add_income(income_category, money, date, file_name):
            
            if(date not in Menu.d.keys()):
                Menu.d[date] = []
                current = [money,income_category, " New Income"]
                Menu.d[date].append(current)
                print(Menu.d)
                return 
            for key in Menu.d:
                if(key == date):
                    Menu.d[key].append([money,income_category, " New Income"])
                    print(Menu.d)
                    break



    @staticmethod
    def add_expense(expense_category, money, date, all_user_data):
            
            if(date not in Menu.d.keys()):
                Menu.d[date] = []
                current = [money,expense_category, " New Expense"]
                Menu.d[date].append(current)
                print(Menu.d)
                return 
            for key in Menu.d:
                if(key == date):
                    Menu.d[key].append([money,expense_category, " New Expense"])
                    print(Menu.d)
                    break

    

Menu.add_expense("clothes", "14", "24-05-2019","money_tracker.txt")
Menu.add_income("Salary", "14440", "24-05-2019","money_tracker.txt")


def main():
    p = input()
    while p != "6" :
        if(p == "1"):
            Menu.list_user_data()
        elif(p == "2"):
            Menu.list_user_data("24-05-2019")
        elif(p == "3"):
            Menu.show_user_expenses()        
        elif(p == "4"):
        
        elif(p == "5"):

        elif(p == "6"):

        else:
            print("Wrong input")       

        p = input()

if(__name__ == "__main__"):
    main()