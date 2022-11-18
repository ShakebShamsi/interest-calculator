def main():
    print("")
    print("This is a monthly loan payment calculator")
    print("")


    principal = float(input("Input the loan amount:₹"))
    apr = float(input("Input the annual interest rate(%): "))
    year = int(input("Input amount of years: "))

    monthly_interest_rate = apr/1200
    amount_of_months = year * 12
    monthly_payment = principal * monthly_interest_rate / (1 -(1 + monthly_interest_rate) ** (-amount_of_months))

    print("The monthly payment for this loan is: ₹%.2f " % monthly_payment)

while True:
    main()