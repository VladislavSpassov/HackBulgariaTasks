
import sys
import os

f = open('Notes','r')
print(f)



f.close()
print("We are in file Testing")
print(__name__)
def user_age(username):
    return 25


def calc(num1,num2):
    print("")
    return num1 + num2


if(__name__ == '__main__'):
    arguments = sys.argv
    print(arguments)
    print("")


print(os.getcwd())

#with open('Notes','r') as f:
 #   print(f.read())



try:

    user_name = Vlado + "Spasov"
    #user_name = Vlado + "Spasov"
#except (ZeroDivisionError,NameError) as exc:
 #   print(exc)

#except NameError as exc:
 #   print(exc)

#except ValueError as exc:
 #   print(exc)

#except TypeError as exc:
 #   print(exc)
    


except Exception as ecs:
    print(ecs)

    raise RunTimeError 