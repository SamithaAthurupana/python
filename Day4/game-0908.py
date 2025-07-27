#write secret num
#get a input
#gess the secret num
#you have 3 chance

finalCountOfAttempt = 3
maxAttempt = 0
secretNum = int(input("Enter your Number: "))
while maxAttempt < finalCountOfAttempt:
    if secretNum != finalCountOfAttempt:
        print("Wrong number!...")
        if secretNum > 3:
            print("Too high!...")
        else:
            print("Too Low!...")
        secretNum = int(input("Enter your Number: "))
        maxAttempt += 1
    else:
        print("You are guess the number!...")
        break
    print("game over")
exit()

