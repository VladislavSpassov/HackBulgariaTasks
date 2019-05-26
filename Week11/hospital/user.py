from hospital.validators import validators



class User:
    from database_layer.queries import Database

    def __init__(self, username, password, status):
        self.username = username
        self.password = password
        self.status = status

    db = Database("Database")

    @classmethod
    def find(cls, username, password):
        from database_layer.queries import Database

        result = cls.db.find_user(username, password)
        if result:
            return cls(username, password, result)

    @classmethod
    def create_new_user(cls, username, hashed_pass, status, *args):
        from database_layer.queries import Database
        ##try:
            # TODO check kwargs

        if(status == "Patient"):
            return cls.db.create_user(username,hashed_pass,status,args[0],args[1],args[2],args[3])        

        elif(status == "Doctor"):
            return cls.db.create_user(username,hashed_pass,status,args[0])        

        #except DatabaseConnectionError:
            #sys.exit(1)
        #return cls(username, hashed_pass,status,**kwargs)
    @staticmethod
    def show_members(current_user):
        User.db.show_members(current_user.status)
'''
    @property
    def status:
        return self._status


'''
