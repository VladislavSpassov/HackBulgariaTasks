from hospital.user import User


class Patient(User):
    def __init__(self,username, password, age,full_name,address,health_status,status=None):
        User.__init__(username,password,status)
        self.age = age
        self.full_name = full_name
        self.address = address
        self.health_status = health_status
    @staticmethod
    def show_available_slots():
        User.db.show_available_slots()


    @staticmethod
    def make_reservation(ID,current_user):
        User.db.make_reservation(ID,current_user)