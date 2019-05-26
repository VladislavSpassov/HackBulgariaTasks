def validate_password(password):
        if(len(password) <= 8):
            print("Your password should be long more than 8 characters")
            raise Exception("Your password should be long more than 8 characters")

        if(password.islower()):
            raise Exception("Your password should have at least 1 Capital letter")
            print("Your password should have at least 1 upper case letter")
        if(all([x >= 'a' and x <= 'z' or x>='A' and x <= 'Z' for x in password])):
            raise Exception("Your password should have at least 1 symbol different from letter ")

def validate_username(user_name):
    if(len(user_name) < 5):
        raise Exception("Too short user name")
    elif(len(user_name) > 15):
        raise Exception("Too long user name")