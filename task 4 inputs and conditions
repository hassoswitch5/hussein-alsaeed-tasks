#PROBLEM 1


grade = float(input("Enter your exam grade out of 100: "))

if 90 <= grade <= 100:
    print("Your grade is A")
elif 80 <= grade < 90:
    print("Your grade is B")
elif 70 <= grade < 80:
    print("Your grade is C")
elif 60 <= grade < 70:
    print("Your grade is D")
elif 0 <= grade < 60:
    print("Your grade is F")
else:
    print("Invalid Degree")

#PROBLEM 2

num1 = float(input("pls enter the first number you want to calculate "))
oper2 = (input("what is the operatator you want to use "))

num2 = float(input("pls enter the second number you want to calculate "))

if oper2 == "+":
    print(num1+num2)
elif oper2 == "-":
    print(num1-num2)

if oper2 == "*":
    print(num1*num2)
elif oper2 == "/":
    print(num1/num2)


#task3

loan = float(input("Please enter your loan amount: "))
age = int(input("Please enter your age: "))
monthly_income = float(input("Please enter your monthly income: "))
employment_status = input("Enter your Employment status (employed/unemployed): ").strip().lower()
Credit_score = float(input("Enter your Credit Score: "))
Outstanding_score = input("Do you have any outstanding Loans (yes/no): ").strip().lower()

reasons = ""
eligible = True

if age < 18:
    eligible = False
    reasons += "Not old enough. "
    
if monthly_income < loan / 12:
    eligible = False
    reasons += "Insufficient income. "
    
if employment_status!= 'employed':
    eligible = False
    reasons += "Unemployed status. "
    
if Credit_score < 350 :
    eligible = False
    reasons += "Low credit score. "

if  Credit_score > 800:
    eligible = False
    reasons += "\Very high credit score. "
    
if Outstanding_score == "yes":
    eligible = False
    reasons += "Outstanding loan. "

if eligible:
    print("You are eligible to apply.")
else:
    print(f"You are not eligible to apply and the reasons are: {reasons}")


