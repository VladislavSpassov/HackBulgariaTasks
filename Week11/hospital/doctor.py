from hospital.user import User

class Doctor(User):
    def __init__(self, username, password, status,title):
        User.__init__(username,password,status)
        self.title = title

    @classmethod
    def add_slot(cls,current_user,start_hour,end_hour,data):
        User.db.add_slot(current_user,start_hour,end_hour,data)

    @classmethod
    def show_slots(cls,current_user):   
        User.db.show_slots(current_user)

    @classmethod
    def delete_slot(cls,current_user,option):
        User.db.delete_slot(current_user,option)

    @classmethod
    def show_pending_reservations(cls,current_user):
        User.db.show_pending_reservations(current_user)