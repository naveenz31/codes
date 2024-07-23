salary=int(input("enter your salary :"))
age=int(input("Enter your Age :"))
if(salary>=20000 or age<=25):
    loan=int(input("enter the required loan amount :"))
    if(loan<=50000):
        print("You are Eligible for Loan")
    else:
        print("Maximum loan amount is 50000")
else:
    print("You are not eligible for Loan")
