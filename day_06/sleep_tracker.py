sleep_hours = []

input("Did you sleep yesterday? ( Enter y/n  ) ")

for i in range(7):
    user_input = int(input(f"{i+1}. day how many hours did you sleep? : "))
    sleep_hours.append(user_input)
'''    if user_input > 8:
        print(eight_hour.append(1))'''

print("=============================")
print("Sleep hours list: ", sleep_hours)

print("=============================")
sum_sleep = sum(sleep_hours)
average_sleep =(sum_sleep/7)
#print(f"average sleep you took : {sum(sleep_hours) // len(sleep_hours)}
print("last 7 days average of sleep: ",average_sleep.__round__(3))
print("=============================")
over_8hours = [hours for hours in sleep_hours if hours > 8]
'''over_8hours = []
for hours in sleep_hours:
    if hours > 8:
        over_8hours.append(hours)'''
print(len(over_8hours))
