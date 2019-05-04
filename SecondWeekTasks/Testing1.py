import Testing

#from Testing import user_age # WE IMPORT CONCRETE FUNCTION FROM OTHER MODULE
#from Testing import * 


__name__ = '__main__'


from Testing import user_age, calc
print(Testing.user_age("Ivan"))


def main():
    print("In Testing2")



if __name__ == '__main__':
    main()
