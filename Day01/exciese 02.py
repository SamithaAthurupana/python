#print your name
#print your name 5 times using single print statement
#print dogs, cats, birds separated by"?"
#print 2 sentences in two different lines using single print statement
#declare three string variables
#print them using string formating
#declare str, int, boolean, float variables and print the type of the variables
from webbrowser import open_new

print("samitha")
print("samitha "*5)
print("Dogs","Cats","Birds", sep='?')
print("First Sentence\nSecond Sentence")

one = "FirstString"
two = "SecondString"
three = "ThirdString"
print(f"First String is: {one} | Second string is: {two} | Third string is: {three}")


firstStr = "String"
age = 26
men = True
hight = 321.2

print(type(firstStr))
print(type(men))
print(type(age))
print(type(hight))
print(f'{type(firstStr)}{type(men)}{type(firstStr)}{type(hight)}')