'''
The TidBit Computer Store has a credit plan for computer purchases. There is a
10% down payment and an annual interest rate of 12%. Monthly payments are 5%
of the listed purchase price minus the down payment. Write a program that takes
the purchase price as input. The program should display a table, with appropriate
headers, of a payment schedule for the lifetime of the loan. Each row of the table
should contain the following items:
n The month number (beginning with 1)
n The current total balance owed
n The interest owed for that month
n The amount of principal owed for that month
n The payment for that month
n The balance remaining after payment
The amount of interest for a month is equal to balance * rate / 12. The amount of
principal for a month is equal to the monthly payment minus the interest owed
'''
purchase_price = int(input("Enter purchase price :"))
down_payment   = (purchase_price * 10) / 100
month = 0
month_interest = 12/12

balance_due = purchase_price - down_payment
while balance_due > 0:
    current_balance = balance_due
    current_interest= ((balance_due * month_interest) / 100)
    principal_due   = balance_due + current_interest
    amount_paid     = (purchase_price * 0.05)
    if amount_paid > principal_due:amount_paid = principal_due
    balance_due     = principal_due - amount_paid
    month += 1


    print("Month No :{} current due :{} month interest :{} principal :{} amount paid :{} balance due :{} ".format(month, current_balance,current_interest,principal_due,amount_paid,balance_due))




