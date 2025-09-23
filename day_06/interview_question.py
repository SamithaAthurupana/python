# palindrome words checker

#1st Method
'''user_input = input("Enter your word: ")

char_arr = []

for letter in user_input: #iterating over each letter in the input word
    char_arr.append(letter)

reversed_arr = char_arr[:] #copying the char_arr
reversed_arr.reverse() #reversing the elements

if char_arr == reversed_arr: #checking reversed array equals to initial character array
    print("palindome")'''

#2nd Method
user_input = input("Enter your word: ")

if user_input == user_input[::-1]:
    print("palindrome ")
else:
    print("Not palindrome")
