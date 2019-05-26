import sqlite3

connection = sqlite3.connect("HospitalManagerDatabase.db")

cursor = connection.cursor()

class Database:

    def __init__(self,name = None):
        self.name = name
        self.create_tables()
    
    def create_tables(self):
        cursor.execute('''

            CREATE TABLE IF NOT EXISTS User(id INTEGER PRIMARY KEY NOT NULL, user_name TEXT, password TEXT, status TEXT)

            '''
            )
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS Patient(id_patient INTEGER PRIMARY KEY NOT NULL,id_user INTEGER , age INTEGER, full_name TEXT,address TEXT,health_status TEXT, FOREIGN KEY (id_user) REFERENCES User(id))
            ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Doctor(id_doctor INTEGER PRIMARY KEY NOT NULL,id_user INTEGER, title TEXT, FOREIGN KEY (id_user) REFERENCES User(id),FOREIGN KEY (id_doctor) REFERENCES Slots(doctorID))
            ''')
        cursor.execute('''
            
            CREATE TABLE IF NOT EXISTS Reservations(id_slot INTEGER NOT NULL , status TEXT, id_patient  INTEGER, FOREIGN KEY (id_patient) REFERENCES Patient(id_patient), FOREIGN KEY (id_slot) REFERENCES Slots(id)) 
            ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Slots(doctorID INTEGER, start_hour TEXT, end_hour TEXT, data TEXT,is_reserved BOOLEAN Default 0, id_reservation INTEGER, id INTEGER PRIMARY KEY NOT NULL)
            ''')
    
    def find_user(self,user_name,password):
        #from HospitalExample.main_controller import MainController
        cursor.execute(
            '''
            SELECT user_name,password,status FROM User WHERE user_name = "{0}" and password = "{1}"
            '''.format(user_name,password))
        rows = cursor.fetchall()
        is_found = False
        print(rows)
        if(len(rows) == 0):
            for row in rows:
                is_found = True
            
        


    def create_user(self,user_name,password,status,*args):
        cursor.execute('''
            INSERT INTO User(user_name,password,status) VALUES("{0}","{1}","{2}")

            '''.format(user_name,password,status))
        connection.commit()


        cursor.execute('''
            SELECT id FROM User WHERE user_name = "{0}"
            '''.format(user_name))

        rows = cursor.fetchall()
        for row in rows:
            ID = row[0]

        if(status == "Patient"):
            vals = []
            for value in args:
                vals.append(value)
            cursor.execute('''
            INSERT INTO Patient(id_user,age,full_name,address,health_status) VALUES("{0}","{1}","{2}","{3}","{4}")

            '''.format(ID,vals[0],vals[1],vals[2],vals[3]))

        elif(status == "Doctor"):
            vals = []
            for value in args:
                vals.append(value)
            cursor.execute('''
            INSERT INTO Doctor(id_user,title) VALUES("{0}","{1}")

            '''.format(ID,vals[0]))
        connection.commit()

    def show_members(self,status):
        print("Database:", status)
        if(status == "Doctor"):
            cursor.execute('''
                SELECT full_name,age,health_status FROM Patient 
                ''')
            rows = cursor.fetchall()
            print(rows)
        elif(status == "Patient"):
            cursor.execute('''
                SELECT Doctor.title,User.user_name FROM Doctor INNER JOIN User ON Doctor.id_user = User.id
                ''')
            rows = cursor.fetchall()
            print(rows)


    def add_slot(self,current_user,start_hour,end_hour,data):
        cursor.execute('''
            SELECT Doctor.id_doctor FROM User INNER JOIN Doctor ON Doctor.id_user = User.id
            ''')

        rows = cursor.fetchall()
        print(rows)
        id_doctor = 0
        for row in rows:
            id_doctor = row[0]

        cursor.execute('''
            SELECT doctorID,start_hour,end_hour,data FROM Slots WHERE start_hour = "{0}" and end_hour = "{1}" and data = "{2}" and doctorID = "{3}"
            '''.format(start_hour, end_hour,data,id_doctor))

        rows = cursor.fetchall()
        if(len(rows) != 0):
            raise Exception("The Slot already exist")

        reserved = False
        cursor.execute('''
            INSERT INTO Slots(doctorID,start_hour,end_hour,data) VALUES("{0}","{1}","{2}","{3}")  

            '''.format(id_doctor,start_hour,end_hour,data))

        connection.commit()
    def show_slots(self,current_user):
        cursor.execute('''
            SELECT Doctor.id_doctor FROM User INNER JOIN Doctor ON Doctor.id_user = User.id
            ''')

        rows = cursor.fetchall()
        print(rows)
        id_doctor = 0
        for row in rows:
            id_doctor = row[0]

        cursor.execute('''
            SELECT * FROM Slots WHERE doctorID = "{0}"
            '''.format(id_doctor))

        rows = cursor.fetchall()

        print(rows)

    def delete_slot(cls,current_user,option):

        cursor.execute('''
            DELETE FROM Slots WHERE id = "{0}"
            '''.format(option))

        connection.commit()

    def show_available_slots(self):
        cursor.execute('''

            SELECT Slots.id,User.user_name,Doctor.title,Slots.start_hour,Slots.end_hour,Slots.data FROM Slots INNER JOIN Doctor on Slots.doctorID = Doctor.id_doctor INNER JOIN User ON User.id = Doctor.id_user 
            ''')

        rows = cursor.fetchall()
        print(rows)

    def make_reservation(self,ID,current_user):
        cursor.execute('''
        SELECT Patient.id_patient FROM User INNER JOIN Patient ON Patient.id_user = User.id
            
        ''')

        rows = cursor.fetchall()
        print(rows)
        id_patient = 0
        for row in rows:
            id_patient = row[0]

        print(id_patient)
        cursor.execute('''

            SELECT * FROM Slots WHERE is_reserved = 0
            ''')

        rows = cursor.fetchall()
        print(rows)
        status = "pending"
        for row in rows:
            print(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

            if(row[6] == int(ID)):
                cursor.execute('''
                INSERT INTO Reservations Values("{0}","{1}","{2}")

                    '''.format(ID,status,id_patient))

                connection.commit()

                print("You made successful reservation request!")
                return

    @classmethod
    def show_pending_reservations(cls,current_user):
        cursor.execute('''
            SELECT Doctor.id_doctor FROM User INNER JOIN Doctor ON Doctor.id_user = User.id WHERE User.user_name = "{0}"
            '''.format(current_user.username))

        rows = cursor.fetchall()
        print(rows)
        id_doctor = 0
        for row in rows:
            id_doctor = row[0]


        cursor.execute('''
            SELECT Patient.full_name,Slots.start_hour,Slots.end_hour,Slots.data,Slots.id FROM Slots INNER JOIN Reservations on Slots.id = Reservations.id_slot INNER JOIN Patient ON Patient.id_patient = Reservations.id_patient
            WHERE Reservations.status = "pending" and Slots.doctorID
            ''')

        rows = cursor.fetchall()
        print(rows)
    @classmethod
    def make_reservation(cls,current_user):
        pass