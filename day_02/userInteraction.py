#1
'''user_input = input("Enter your Name : ") #print("Enter your Name : ") with prompt
user_age = input("Enter your age: ")
print(f"My Name: {user_input} & My Age: {user_age}")'''

#When user gives the birth year, you should print his age
'''current_year = 2025
user_input = int(input("Enter your Birth Year : "))
age = (current_year - user_input)
print(f"Now your age is: ",age)'''

#3
#One box can contain 12 eggs, when user inputs no of eggs calculate how many boxes
#boxes should be filled print remaining amount as well
'''box_size = 12
user_input = int(input("How many Eggs: "))
box_count1 = int(user_input/box_size)
box_count2 = (user_input % box_size)
print(f"Boxes count: ", box_count1)
print(f"Remaining boxes: ", box_count2)'''

#4
#Take the principal amount
#intrest percentage
#for how many years
intrest_percentage= 10
intrest_years = float(5)
principal_amount = float(input("What is the Amount: "))
final_amount= ((principal_amount*intrest_percentage)/100) *  intrest_years
print(final_amount)

#5
#when user inputs no of minutes, we should output no of hours and remaining minutes
'''hour = int(60)
no_minutes=int(input("Enter Number of minutes: "))
final_Out = float(no_minutes / hour)
print(f"Number Of Hours",final_Out,)'''