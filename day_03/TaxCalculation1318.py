'''annualIncome = float(input("Enter your salary: "))

if annualIncome <= 1200000:
    print("You have no tax")
else:
    taxableIncome = annualIncome - 1200000

    if taxableIncome <= 500000:
        tax = taxableIncome * 0.06
    elif taxableIncome <= 1000000:
        tax = (500000 * 0.06) + ((taxableIncome - 500000) * 0.12)
    elif taxableIncome <= 1500000:
        tax = (500000 * 0.06) + (500000 * 0.12) + ((taxableIncome - 1000000) * 0.18)
    elif taxableIncome <= 2000000:
        tax = (500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + ((taxableIncome - 1500000) * 0.24)
    elif taxableIncome <= 2500000:
        tax = (500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (500000 * 0.24) + ((taxableIncome - 2000000) * 0.30)
    else:
        tax = (500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (500000 * 0.24) + (500000 * 0.30) + ((taxableIncome - 2500000) * 0.36)

    print("Your annual tax is:", tax)'''

monthlyIncome = float(input("Enter your monthly salary: "))

# Calculate annual income
annualIncome = monthlyIncome * 12

# Check tax-free threshold
if annualIncome <= 1200000:
    print("You have no tax")
    print("Your final monthly salary is:", monthlyIncome)
else:
    taxableIncome = annualIncome - 1200000

    if taxableIncome <= 500000:
        tax = taxableIncome * 0.06

    elif taxableIncome <= 1000000:
        tax = (500000 * 0.06) + ((taxableIncome - 500000) * 0.12)

    elif taxableIncome <= 1500000:
        tax = (500000 * 0.06) + (500000 * 0.12) + ((taxableIncome - 1000000) * 0.18)

    elif taxableIncome <= 2000000:
        tax = (500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + ((taxableIncome - 1500000) * 0.24)

    elif taxableIncome <= 2500000:
        tax = (500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (500000 * 0.24) + ((taxableIncome - 2000000) * 0.30)

    else:
        tax = (500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (500000 * 0.24) + (500000 * 0.30) + ((taxableIncome - 2500000) * 0.36)

    # Calculate post-tax annual income and monthly salary
    netAnnualIncome = annualIncome - tax
    netMonthlyIncome = netAnnualIncome / 12

    print("Your annual tax is:", tax)
    print("Your monthly salary after tax is:", netMonthlyIncome)

