import hashlib
from hospital.validators import validators 
from hospital.user import User
from hospital.doctor import Doctor

class MainController:

    @classmethod
    def sign_in(cls, username, password):
        cls._password_validate(password)
        password = cls._hash_password(password)
        current_user = User.find(username, password)
        return current_user

    @classmethod
    def sign_up(cls, username, password, second_password,status,**kwags):

        cls._password_validate(password)
        cls._password_validate(second_password)

        hashed_pass1 = cls._hash_password(password)
        hassed_pass2 = cls._hash_password(second_password)
        cls._do_passwords_match(hashed_pass1, hassed_pass2)

        if User.find(username, hashed_pass1):
            raise Exception("User already exist")

        if(status == "Doctor"):
            return User.create_new_user(username, hashed_pass1,status,kwags["title"])
        elif(status == "Patient"):
            return User.create_new_user(username,hashed_pass1,status,kwags.pop("age"),kwags.pop("full_name"),kwags.pop("address"),kwags.pop("health_status"))        

    @classmethod
    def show_members(cls, current_user):
        if current_user.status == "Doctor":
            return cls.show_patients(current_user)
            #  [Patient('Roza'), Patient('Mimi')]
        elif current_user.status == "Patient":
            return cls.show_doctors(current_user)
    @classmethod
    def show_slots(cls,current_user):
        from hospital.doctor import Doctor
        Doctor.show_slots(current_user)
    def show_patients(current_user):
        User.show_members(current_user)

    def show_doctors(current_user):
        User.show_members(current_user)


    @staticmethod
    def show_available_slots():
        from hospital.patient import Patient

        Patient.show_available_slots()

    @staticmethod
    def make_reservation(ID,current_user):

        from hospital.patient import Patient

        Patient.make_reservation(ID,current_user)


    @staticmethod
    def show_pending_reservations(current_user):
        from hospital.doctor import Doctor

        Doctor.show_pending_reservations(current_user)
    @staticmethod
    def delete_slot(current_user,ID):
        Doctor.delete_slot(current_user,ID)

    @classmethod
    def add_slot(cls,current_user,start_hour,end_hour,date):
        from hospital.doctor import Doctor
        Doctor.add_slot(current_user,start_hour,end_hour,date)
    

    def _hash_password(password):

        h = hashlib.md5(password.encode())
        return h.hexdigest()
    

    @classmethod
    def _do_passwords_match(cls,password, second_password):
        if(cls._hash_password(password) == cls._hash_password(second_password)):
            return True
        return False    

    @staticmethod
    def _password_validate(password):
        validators.validate_password(password)