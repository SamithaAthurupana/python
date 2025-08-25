def nic_checker(user_nic):
    if len(user_nic) != 10:  # should be 10, not 11
        return False
    if user_nic[0:9].isdigit() and user_nic[-1].upper() == "V":
        return True
    return False

user_nic = "123456789V"

if nic_checker(user_nic):
    print("nic is valid")
else:
    print("nic not valid")
from operator import index


print("----------------------")

user_mail = input("Enter email: ")

def email_checker(user_mail):

    if "@" not in user_mail:
        return False
    elif user_mail.index('@') != 0 and user_mail.index("@") != len(user_mail) -1:
        return True
    else:
        return False


print(email_checker(user_mail))


