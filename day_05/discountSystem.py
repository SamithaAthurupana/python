#bill value < 5000
#can not use coupon
#is member
#20% discount

'''buyingVegitable = input("are you buying vegitable? yes/no: ") == "yes"
inMember = input("Do you have Member Id: ") == "yes"
isUsingCoupon = input("Are you using coupon? : yes/no: ") == "yes"


if inMember and not buyingVegitable and not isUsingCoupon:
    print("lets check the bill...")
    checkBillValue = int(input("Enter bill value: "))<5000
    print("you are not eligible for the 20% discount")
else:
    print("You are eligible discount")'''

in_member = input("Do you have Member Id? yes/no: ") == "yes"
buying_vegetable = input("Are you buying vegetables? yes/no: ") == "yes"
is_using_coupon = input("Are you using a coupon? yes/no: ") == "yes"
bill_value = int(input("Enter bill value: "))

if (in_member
        and not buying_vegetable
        and not is_using_coupon
        and bill_value > 5000):
    print("You are eligible for a 20% discount.")
    print(f"You get a discount Rs: {bill_value * (20/100)}/=")
else:
    print("You are not eligible for the 20% discount.")




