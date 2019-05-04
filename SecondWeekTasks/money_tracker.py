import sys
import os
import re


def list_user_data(all_user_data):
    for k in all_user_data:
        print('-----------------',k,'------------------')
        for v in all_user_data[k]:
            print(v)
            print(all_user_data[k][v])



def show_user_incomes(all_user_data):
    result = []
    for k in all_user_data:
        for v in all_user_data[k]:
            if(v == "income"):
               result.append(all_user_data[k][v])

    return result


def show_user_savings(all_user_data):
    result = []
    for k in all_user_data:
        for v in all_user_data[k].values():
            for s in v:
                if(s[1] == "Savings"):
                    result.append(s)
    return result


def show_user_deposits(all_user_data):
    result = []
    for k in all_user_data:
        for v in all_user_data[k].values():
            for s in v:
                if(s[1] == "Deposit"):
                    result.append(s)
    return result

    '''    with open(all_user_data,'r') as f:

        result = []
        for x in f:
            if("Deposit" in x):
                result.append(x)

        print("\n".join(result))
    '''
    


def show_user_expenses(all_user_data):
    result = []
    print(all_user_data)
    for v in all_user_data.values():
        for k in v:
            if(k == "expense"):
                for v1 in v[k]:
                    result.append(v1)
                    
            
        
    return result
    

def list_user_expenses_ordered_by_categories(all_user_data):
    print(all_user_data)
    result = show_user_expenses(all_user_data)
    print(result)
    newResult = []
    for index in range(len(result)):
        ind = index
        for ind in range(len(result)):
            
            if(result[index][1] > result[ind][1]):
                temp = result[index]
                result[index] = result[ind]
                result[ind] = temp

    print(result)
    result.reverse()
    print(result)
    return result

def show_user_data_per_date(date, all_user_data):
    for d in all_user_data:
        if(date == d):
            return (all_user_data[d])
            break



def list_income_categories(all_user_data):
    incomeCategories = []
    for v in all_user_data.values():
        for k in v:
            if(k == "income"):
                for v1 in v[k]:
                    if(v1[1] not in incomeCategories):

                        incomeCategories.append(v1[1])
    return incomeCategories



def list_expense_categories(all_user_data):
    expenseCategories = []
    for v in all_user_data.values():
        for k in v:
            if(k == "expense"):
                for v1 in v[k]:
                    if(v1[1] not in expenseCategories):

                        expenseCategories.append(v1[1])
    return expenseCategories



def add_income(income_category, money, date, all_user_data):
    pass


def add_expense(expense_category, money, date, all_user_data):
    pass


#list_user_data('/home/vladislavspassov/Desktop/Python101/08.03.2019/money_tracker.txt')
#show_user_incomes('/home/vladislavspassov/Desktop/Python101/08.03.2019/money_tracker.txt')
#print('------------------')
#show_user_deposits('/home/vladislavspassov/Desktop/Python101/08.03.2019/money_tracker.txt')
#print('------------------')
#show_user_expenses('/home/vladislavspassov/Desktop/Python101/08.03.2019/money_tracker.txt')


def main():
     all_user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
     inp = {'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}}
     #list_user_data(all_user_data)
     #print('------------------')
     #print(show_user_incomes(all_user_data))
     #print(show_user_savings(all_user_data))
     #print(show_user_deposits(all_user_data))
     #print('------------------')
     #print(show_user_expenses(all_user_data))
     #list_user_expenses_ordered_by_categories(inp)
     print(show_user_data_per_date('22-03-2019', all_user_data))
     print(list_income_categories(all_user_data))
     print(list_expense_categories(inp))
if(__name__ == "__main__"):
    main()