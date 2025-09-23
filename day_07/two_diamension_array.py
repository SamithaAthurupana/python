'''i = []

for i in range(4):
    for x in range(4):
        print("A")
    print("A")
    '''
from operator import index

from day_06.students_grading_system import total

'''
two_dim_array = [["x","x","x","x"],
                 ["x","x","x","x"],
                 ["x","x","x","x"],
                 ["x","x","x","x"]]


two_dim_array[1][1] = "b"
print(two_dim_array)

for x in two_dim_array:
    print(x)
    for y in x:
        print(y)


print(two_dim_array)
'''

# whether tracking
#for each hour in a day we track the temperature we do this for 31 Days
import time

temps_per_day_for_month = [[0.0 for _ in range(3)] for _ in range(7)] # _ variable name

while True:
    print(""
          "1. Add Temp press"
          "2. view temp for a day"
          "3. get avg"
          "4. max"
          "5.")
    user_input = int(input("Enter the menu number: "))

    if user_input == 1:
        day = int(input("Enter a day from ( 1 - 7 ): ")) - 1
        hour = int(input("Enter a hour from ( 1 - 3 ): ")) - 1
        temp = int(input("Enter a temp: ")) - 1

        temps_per_day_for_month[day][hour] = temp


        for temps_per_days in temps_per_day_for_month:
            print(temps_per_days)
        time.sleep(2)

    if user_input == 2:
        day = int(input("Enter a day from ( 1 - 7 ): ")) - 1
        hour = int(input("Enter a hour from ( 1 - 3 ): ")) - 1

        print(f"temperature for day - {day+1} and hour - {hour + 1} is : {temps_per_day_for_month[day][hour]}")
    if user_input == 3:

        day = int(input("Enter a day from ( 1 - 7 ): ")) - 1

        temps_for_day = temps_per_day_for_month[day]

        print(f"Average Temp: {sum(temps_for_day)/3}")
        print(temps_for_day)
    if user_input == 4:
        #Highest value
        day = int(input("Enter a day from ( 1 - 7 ): ")) - 1
        highest_value = temps_per_day_for_month[day]
        print(f"Max value of the day: {max(highest_value)}")
    if user_input == 5:
        day = int(input("Enter a day from ( 1 - 7 ): ")) - 1
        #first method
        temps_for_day = temps_per_day_for_month[day]
        max_temp = (f"Max temp was: {max_temp} at {temps_for_day.index(max_temp) + 1}")
       # second method
        hottest_temp = temps_for_day[0]
        hottest_day = 0
        for i in range(len(temps_for_day)):
            if temps_for_day[i] > hottest_temp:
                hottest_temp = temps_for_day[i]
                hottest_day = i
        print(f"===with for loop=== Max temp was {hottest_temp} at {hottest_day + 1}")
    if user_input == 6:
        '''total = 0
        for temps in temps_per_day_for_month:
            for temp in temps:
                total += temp
        print(f"average temperature for the week {total/21}")'''

        total = 0
        flattend_2d_arry = []

        for temps in temps_per_day_for_month:
            for temp in temps:
                flattend_2d_arry.append(temp)
        print(f"average temperature for the week {flattend_2d_arry / 21}")





