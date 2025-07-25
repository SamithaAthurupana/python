#declare two integer variables
#perform all the arithmetic operators and print
import math

numberOne =  2
numberTwo = 2

addition = (numberOne + numberTwo)
subtraction = (numberOne - numberTwo)
multiplication = (numberOne * numberTwo)
division = (numberOne / numberTwo)
modules = (numberOne % numberTwo)
exponentiation = (numberOne ** numberTwo)
floorDivision = (numberOne // numberTwo)

print(f"Performing addition : {addition}")
print(f"Performing subtraction : {subtraction}")
print(f"Performing multiplication : {multiplication}")
print(f"Performing division : {division}")
print(f"Performing Module : {modules}")
print(f"Performing Exponentiation : {exponentiation}")
print(f"Performing Floor division : {floorDivision}")

print((5 * (25 % 13 + 100) / (2 * 13)) // 2)
print((2 ** 4) , (2 * 4.) , (2 * 4))
print(2 * 3 % 5) #Same priority for the % and * then start from left side

numOne = 4
numTwo = 2
print("Square Root = ",(numOne ** 2 + numTwo ** 2) ** 0.5)
squareRoot= math.sqrt(numOne ** 2 + numTwo ** 2)
print(f"Square Root = {squareRoot}")
print(round(squareRoot, 3)) #Reduce decimal points using round keyword