'''import time

print("----- Age calculating system -----\n")

current_year = 2025

name = input("Enter your name: ")
age = int(input("Enter age: "))
print("calculating....")
time.sleep(3)

def age_base_on_year(current_year,age):
    now_age = current_year - age
    if now_age > 25:
        print("you are too old because, ")
    elif now_age > 13:
        print("Now you are teen because, ")
    else:
        print("still you are child because, ")

age_base_on_year(current_year,age)

def now_age(current_year, age):
    date_of_year = current_year - age
    print(f"your birth year is: {date_of_year}")

now_age(current_year, age)
'''
"""
first write a function to calculate age based on current year and birth year.
if age < 13
    return teen 
age < 20 teen
less than 50 "adult"

age > 50 return senior citizen

write a function to get age_status based on the age.  
"""

print("----- Age Calculator ------")

def current_age(current_year,birth_year):
    return current_year - birth_year

def age_sts(age):
    if age < 13:
        return "teen"
    elif 13 < age < 20:
        return "Teen"
    elif age < 50:
        return "Adult"
    else:
        return f"{age}'s"

def main():
    this_year = int(input("Enter the current year: "))
    year_of_birth = int(input("Enter your birth year: "))
    user_current_age = current_age(current_year=this_year, birth_year=year_of_birth)

    print(f"Your current age is: {user_current_age}")
    print(f"Your age status: {age_sts(age=user_current_age)}")

main()
