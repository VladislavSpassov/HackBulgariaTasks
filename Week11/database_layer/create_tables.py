import sqlite3
from HospitalExample.controllers main_controller import MainController

connection = sqlite3.connect("HospitalManagerDatabase.db")

cursor = connection.cursor()

class Database:

    @staticmethod
    def create_tables():
        cursor.execute('''

            CREATE TABLE User(id INTEGER PRIMARY KEY NOT NULL, user_name TEXT, password TEXT, status TEXT)

            '''
            )
        cursor.execute(
            '''
            CREATE TABLE Patient(id_patient INTEGER PRIMARY KEY NOT NULL,id_user INTEGER, age INTEGER, full_name TEXT,address TEXT,health_status TEXT, FOREIGN KEY (id_user) REFERENCES User(id))
            ''')
        cursor.execute('''
            CREATE TABLE Doctor(id_doctor INTEGER PRIMARY KEY NOT NULL,id_user INTEGER, title TEXT, FOREIGN KEY (id_user) REFERENCES User(id))
            ''')
        cursor.execute('''
            
            CREATE TABLE Reservations(id_slot INTEGER PRIMARY KEY NOT NULL , status TEXT, id_patient  INTEGER, FOREIGN KEY (id_patient) REFERENCES Patient(id_patient)) 
            ''')
        cursor.execute('''
            CREATE TABLE Slots(doctorID INTEGER, start_hour TEXT, end_hour TEXT, data TEXT,is_reserved BOOLEAN, id INTEGER, FOREIGN KEY (id) REFERENCES  Reservations(id_slot))
            ''')
    @staticmethod
    def find_user(user_name,password):
        cursor.execute(
            '''
            SELECT user_name,password FROM User WHERE user_name = {0} and password = {1}
            '''.format(user_name,MainController._hash_password(password))
        



