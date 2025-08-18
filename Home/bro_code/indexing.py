# indexing = accessing elements of a sequence using [] (indexing operator)
#       [ start : end : step ]

#credit_number = "1234-5678-9012-3456"

#print(credit_number[0])
#print(credit_number[:4]) #print(credit_number[0:4])
#print(credit_number[5:9])
#print(credit_number[0:4])
#print(credit_number[5:])
#print(credit_number[-2])
#print(credit_number[::3]) #every 3rd character

#reverse string
'''credit_number = credit_number[::-1]
print(credit_number)'''

#format specials

price = 3324.1445434
price2 = -892.22

print(f"price is ${price:.1f}")
print(f"price is ${price:.3f}")
print(f"price is ${price:.10}")
print(f"price is ${price:010}")
print(f"price is ${price:+}")
print(f"price is ${price: }")
print(f"price is ${price:,}")
print(f"price is ${price:,.2f}")
print(f"price is ${price:+,.2f}")