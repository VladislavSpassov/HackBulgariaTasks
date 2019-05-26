import sqlite3 

connection = sqlite3.connect("BusinessCardsCatalog.db")

cursor = connection .cursor()

n = 0
def generate_id():
    
    yield n 
    n +=1


def add():
    print("Enter user name:")
    user_name = input()
    print("Enter email:")
    email = input()
    print("Enter age: ")
    age = input()
    print("Enter phone:")
    phone = input()
    print("Enter addional info (optional):")
    add_info = input()
    if(add_info == "no"):
        add_info = ""
    generator = generate_id()
    id = next(generator)
    print(id)

    cursor.execute(
        '''
        insert into User VALUES("{id}","{user_name}","{email}","{age}","{phone}","{add_info}")

        '''.format(id = id ,user_name = user_name,email = email, age = int(age),phone = phone,add_info = add_info))

    connection.commit()
def lst():
    cursor.execute(
        '''
        select * from User;
        ''')
    users_data = cursor.fetchall()
    print(list(users_data))
    connection.commit()
def delete():
    id = input()
    id = int(id)
    cursor.execute(
        '''
        delete from User where id = {id}
        '''.format(id = id))

    users_data = cursor.fetchall()
    print(users_data)
    cursor.execute(
        '''
        select * from User
        ''')
    users_data = cursor.fetchall()
    print(users_data)

    connection.commit()
def get():
    id = input()
    id = int(id)

    cursor.execute("Select * from User where id = {id}".format(id = id))
    users_data = cursor.fetchall()
    print(users_data)

    connection.commit()
def help():
    print('''
1. `add` - insert new business card
2. `list` - list all business cards
3. `delete` - delete a certain business card (`ID` is required)
4. `get` - display full information for a certain business card (`ID` is required)
5. `help` - list all available options
        ''')
def main():
    cursor.execute(
        ''' 
        create table if not exists User(id integer not null primary key unique,full_name text not null unique, email text not null unique, age int not null, phone text not null unique,additional_info text)
        '''
        )
    print("Hello! This is your business card catalog. What would you like? (enter ""help"" to list all available options)")

    while(True):
        i = input()
        if i == "add" :
            add()
        elif i == "list":
            lst()
        elif i == "delete":
            delete()
        elif i == "get":
            get()
        elif i == "help":
            help()
        else:
            print("Not correct command")
            break

if(__name__ == "__main__"):
    main()