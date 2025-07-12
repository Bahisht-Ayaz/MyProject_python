name=input("please enter your name :")
salary=int(input("please enter your salary :"))

print("Expense calculator")
grocery_bill=float(input("Enter your Grocery bill :"))
ke_bill=float(input("Enter your KE bill :"))
gas_bill=float(input("Enter your gas bill :"))
internet=float(input("Enter your internet bill :"))
water_bill=float(input("Enter your water bill :"))
jamadaar=float(input("Enter your jamadaar bill :"))
super_card=float(input("Enter your super card :"))
transport=float(input("Enter your transport :"))
own_house=input("Do you live in your own house :")


if own_house.lower() == "no":
    rent=float(input("Enter your rent"))
else:
    rent = 0

married=input("Are you married ?")
if married.lower() =="yes":
    child=int(input("How many children do you have :"))
    if child > 0:
        child_expense=float(input("Enter your child expense : "))
    else:
        child_expense = 0
total_expenses = grocery_bill + ke_bill + gas_bill + internet + water_bill + jamadaar + super_card + transport + rent +child_expense
total_saving=salary-total_expenses
if salary > total_expenses:
    print(f"{name} your savings are : {total_saving} \nYou should take savings plan \nKindly visit your nearest Meezan Bank")
elif salary == total_expenses:
    print("Please you should take major steps to increase your income and contact dholu bholu")
else:
    print("Please look after your expenses")
print(f"Your salary is : {salary} \n Your total expenses is : {total_expenses} \n Total saving is : {total_saving}")