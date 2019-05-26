import sqlite3
import random
import sys
connection = sqlite3.connect("VehicleRepairManager_new.db")

cursor = connection.cursor()

def register(name):
    print("Are you a client or Mechanic?")
    # I implement it so because i don't use autoincrement
    ID = random.randint(1,60000)    
    
    c_or_m = input()  
    if(c_or_m == "client"):
        cursor.execute("INSERT INTO Client(id) VALUES({0})".format(ID))
        connection.commit()
    elif(c_or_m == "Mechanic"):
        cursor.execute("INSERT INTO Mechanic(id) VALUES({0})".format(ID))
        connection.commit()
    else:
        print("Wrong command") 
        sys.exit(1)
    print("Provide phone_number:")
    phone_number = input()
    print("Provide email:")
    email = input()
    print("Provide address:")
    address = input()

    cursor.execute('''
        INSERT INTO BaseUser VALUES("{0}","{1}","{2}","{3}","{4}")
        '''.format(ID,name,email,int(phone_number),address))
    connection.commit()

    
def client_user_interface(name):
    print('''
Hello, {0}!
You can choose from the following commands:
list_all_free_hours
list_free_hours <date>
save_repair_hour <hour_id>
update_repair_hour <hour_id>
delete_repair_hour <hour_id>
add_vehicle
update_vehicle <vehicle_id>
delete_vehicle <vehicle_id>
exit

        '''.format(name))
    client_id = "SELECT id FROM Client WHERE user_name = {0}".format(name)
    command = input()
    numbers_str = command.split(" ")
    print(command in "save_repair_hour 4")
    are_there_numbers = False 
    for num in numbers_str:
        if(num.isdigit()):
            are_there_numbers = True
    
    
    ############################## TO DO Implement commands with extracting number from string 
    if(command == "list_all_free_hours" and not are_there_numbers):
        cursor.execute("SELECT id,ddate, start_hour FROM RepairHour where status = 1")
        rows = cursor.fetchall()
        print(rows)
    elif(command == "add_vehicle" and not are_there_numbers):
        vehicle_category = input("Vehicle category:")
        vehicle_make = input("Vehicle make:")
        vehicle_model = input("Vehicle model:")
        vehicle_register_number = input("Vehicle register number:")
        gear_box = input("Vehicle gear box:")
        cursor.execute(
            '''
            SELECT id FROM BaseUser where user_name = "{0}"
            '''.format(name))
        rows = cursor.fetchall()
        ID = rows[0][0]
        print(rows)
        print(ID)

        cursor.execute('''
            INSERT INTO Vehicle (category,make,model,register_number,gear_box,owner) VALUES("{0}","{1}","{2}","{3}","{4}","{5}")
            '''.format(vehicle_category,vehicle_make,vehicle_model,vehicle_register_number,gear_box,ID))
            
        connection.commit()
    elif("save_repair_hour" in command and are_there_numbers):
        cursor.execute("SELECT * FROM RepairHour WHERE status = 0")
        rows = cursor.fetchall()
        print("Choice hour by id:")
        print(rows)
        choice = input()

        print("Choose Vehicle to repair:")
        cursor.execute("SELECT * FROM Vehicle INNER JOIN ON Client WHERE id = {0}".format(client_id))
        print(cursor.fetchall())
        cursor.execute("SELECT * from Service")
        print(cursor.fetchall())
        choice = input()
    elif(command == "list_free_hours"):
        print("Date:")
        date = input()
        cursor.execute("SELECT * FROM RepairHour WHERE RepairHour.date = {0}".format(date))
        print(cursor.fetchall())

    elif (command == "update_repair_hour <hour_id>"):
        pass
    elif (command == "delete_repair_hour <hour_id>"):
        pass
    elif(command == "update_vehicle <vehicle_id>"):
        pass
    elif(command == "delete_vehicle <vehicle_id>"):
        pass
    elif(command == "exit"):
        sys.exit(1)
    else:
        print("Your command is not valid. Please try again!")

def mechanic_user_interface(name):
    print('''
        Hello, Mechanic Panda!
        You can choose from the following commands:
        list_all_free_hours
        list_free_hours <date>
        list_all_busy_hours
        list_busy_hours <date>
        add_new_repair_hour
        add_new_service
        update_repair_hour <hour_id>
        exit
        ''')
    command = input("command:")
    if(command == "list_all_free_hours"):
        cursor.execute("SELECT id,ddate, start_hour FROM RepairHour")
        rows = cursor.fetchall()
        print(rows)
    elif(command == "list_free_hours <date>"):
        pass
    elif(command == "list_all_busy_hours"):
        pass
    elif(command == "list_busy_hours <date>"):
        pass
    elif (command == "update_repair_hour <hour_id>"):
        pass
    elif (command == "add_new_repair_hour"):
        date = input("Repair hour date: ")
        hour = input("Start Hour:")

        cursor.execute('''

            INSERT INTO RepairHour(ddate,start_hour) VALUES("{0}","{1}")
            '''.format(date,hour))

        connection.commit()
    elif(command == "add_new_service"):
        pass
    elif(command == "exit"):
        sys.exit(1)
    else:
        print("Your command is not valid. Please try again!")

def main():

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS BaseUser(id INTEGER NOT NULL PRIMARY KEY UNIQUE, user_name TEXT, email TEXT, phone_number INTEGER(10), address TEXT)
        '''
    )
     
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Client(id INTEGER PRIMARY KEY, FOREIGN KEY(id) REFERENCES BaseUser(id));
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Vehicle(id INTEGER NOT NULL PRIMARY KEY, category TEXT, make TEXT, model TEXT, register_number TEXT, gear_box TEXT, owner INTEGER ,FOREIGN KEY(owner) REFERENCES Client(id));
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Mechanic(id INTEGER NOT NULL PRIMARY KEY, base_id INT,title TEXT, FOREIGN KEY(base_id) REFERENCES BaseUser(id));
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Service(id INTEGER PRIMARY KEY NOT NULL , name TEXT );
        '''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS MechanicService(id INTEGER NOT NULL PRIMARY KEY, mechanic_id INT, service_id INT, FOREIGN KEY (service_id) REFERENCES Service(id),FOREIGN KEY(mechanic_id) REFERENCES Mechanic(id));
        '''
    )


    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS RepairHour(id INTEGER PRIMARY KEY NOT NULL, ddate TEXT, start_hour TEXT, vehicle INT ,bill REAL , mechanic_service INT ,FOREIGN KEY(mechanic_service) REFERENCES MechanicService(id),FOREIGN KEY(vehicle) REFERENCES Vehicle(id));
        '''
    )
    connection.commit()
    while True:
        print('''
        Hello!
        Provide user name:
            ''')
        user_name = input()
        cursor.execute("SELECT user_name FROM BaseUser")    
        rows = cursor.fetchall()
        names = [row[0] for row in rows]  
        if user_name == "stop":
            break  
        if(user_name not in names):
            print("Unknown user!")
            print("Would you like to create new user?")
            answer = input()
            if(answer == "yes"):
                register(user_name)
            elif(answer == "no"):
                print("Sorry to see you gone :(")
                break
            else:
                print("Wrong commad")
        
        else:
            is_client = False
            cursor.execute('''
                SELECT * FROM BaseUser INNER JOIN Client on BaseUser.id = Client.id
                '''
                )
            rows = cursor.fetchall()
            names = [row[1] for row in rows]
            for name in names:
                if(name == user_name):
                    is_client = True
                    client_user_interface(user_name)
            

            cursor.execute('''
                SELECT user_name FROM BaseUser INNER JOIN Mechanic on BaseUser.id = Mechanic.base_id
                '''
            )
            if(not is_client):
                mechanic_user_interface(user_name)
        

if(__name__ == "__main__"):
    main()