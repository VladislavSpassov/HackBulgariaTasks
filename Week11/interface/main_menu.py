from controllers.main_controller import MainController


class MainMenu:


    OPTION_MENU_Patient = '''
        1 - show_doctors,
        2 - available_slots
        3 - make reservation

        '''
    OPTION_MENU_Doctor  = '''
        1-add_slot
        2-remove_slot
        3-show_pending_reservations
        4-show_patients
        5-show my slots
        6-accept reservation
        7-cancel reservation
    '''

    @classmethod
    def default_method(cls, *args, **kwargs):
        print('HELP MENU')

    @classmethod
    def show_options(cls,  current_user):
        if(current_user.status == "Doctor"):
            print(MainMenu.OPTION_MENU_Doctor)
            option = input("Please provide us with your choice: ")
            if(option == "1"):
                start_hour = input("Start hour: ")
                end_hour = input("End hour: ")
                date = input("Date : ") 
                MainController.add_slot(current_user,start_hour,end_hour,date)
            elif(option == "2"):
                MainController.show_slots(current_user)
                option = input("choice id for deleting: ")
                MainController.delete_slot(current_user,option)

            elif(option == "3"):
                MainController.show_pending_reservations(current_user)
            elif(option == "4"):
                MainController.show_patients(current_user)

            elif(option == "5"):
                MainController.show_slots(current_user)
            elif(option == "6"):
                MainController.accept_reservation() #TO DO
            else:

                print("Not correct option")
        elif(current_user.status == "Patient"):
            print(MainMenu.OPTION_MENU_Patient)
            option = input("Please provide us with your choice: ")
            if(option == "1"):
                MainController.show_doctors(current_user)
            elif(option == "2"):
                MainController.show_available_slots()
            elif(option == "3"):
                MainController.show_available_slots()
                ID = input("Choose slot: ")
                MainController.make_reservation(ID,current_user) # TO DO
        else:
            print("Status cannot be named this way!")
            sys.exit(1)


        if option == '1':
            MainController.show_members(current_user)
        elif option == "2":
            pass

'''            
    @classmethod
    def  _pretty_print_members(cls, members):
        for member in members:
            print('{status} {username}'.format(
                status=getattr(member, 'status', ''),
                username=member.username
            ))
'''