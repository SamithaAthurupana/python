'''s = "Simplilearn"
for i in s:
    print(i)'''

#S*i*m*p*l*i*l*e*a*r*n*
'''s = "Simplilearn"
for i in s:
    print(i, end="*")'''

#Use for loop in a list
#java Python Ruby HTML
'''programmimg = ["java", "Python", "Ruby", "HTML"]
for iter in programmimg:
    print(iter, end=" ")'''

#Find the avg of a list of numbers
'''list_num = [20,25,10,50,45]
sum = 0
for i in list_num:
    sum = sum + i
print("Sum = ", sum)
print("Average = ", sum/len(list_num))'''

#for loop using a tuple
'''num = (30, 45, 60, 50, 70)
sum = 0
for i in num:
    sum = sum + i
print(sum)'''

#range function
'''ten = 10
for i in range(10):
    print(ten-i, end=" ")'''
'''for i in range(0, 10, 2):
    print(i, end=" ")'''

#to print table of a given number
'''n = int(input("Enter the number: "))
for i in range(1, 11):
    mul = n * i
    print(f"|{n} * {i} = {mul}| " ,end="")'''
#|5 * 1 = 5| |5 * 2 = 10| |5 * 3 = 15| |5 * 4 = 20| |5 * 5 = 25| |5 * 6 = 30| |5 * 7 = 35| |5 * 8 = 40| |5 * 9 = 45| |5 * 10 = 50|

'''list_one = ['C++', 'Java', 'Python', 'R']
for i in range(len(list_one)):
    print("Hello", list_one[i] ,end="  ")'''
# Hello C++  Hello Java  Hello Python  Hello R

#nexted for loop
'''companies = ['google', 'apple', 'pwc', 'uber']
for i in companies:
    print("we will display each letter of "+i)
    for letter in i:
        print(letter)'''

#for loop with else clause
'''for i in range(0, 10, 3):
    print(i, end=" ")
else:
    print("Loop has been end!")'''
#0 3 6 9 Loop has been end!

#break
'''for i in range(0, 10):
    if i == 6:
        break
    print(i, end=" ")'''
# 0 1 2 3 4 5

#continue
'''for i in range(1, 10):
    if i == 6 :
        continue
    print(i, end=" ")'''
#1 2 3 4 5 7 8 9

#program to display the total goals a player has scored
'''player_name = "Carmelo"
goals = {'Edison': 14, 'Bernat': 3, 'Carmelo': 7}

for player in goals:
    if player == player_name:
        print(goals[player])
        break
else:
        print('No player with that name found')'''
#7

# *** cube of the number ***
'''num = [2,5,2,6,8,3]
cube = []
for i in num:
    cube.append(i ** 3)
    print(cube)''' '''
                        [8]
                        [8, 125]
                        [8, 125, 8]
                        [8, 125, 8, 216]
                        [8, 125, 8, 216, 512]
                        [8, 125, 8, 216, 512, 27]
'''

#pattern printing
'''n = int(input("enter the number: "))
for i in range(0, n):
    for j in range(0, i+1):
        print("*", end="")
    print()'''          ''' *
                            **
                            ***
                            ****
                            *****   '''

#
