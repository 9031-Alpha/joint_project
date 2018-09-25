

""" Assignment 1: Alpha Group (7) """
""" Part A """
"""
# Taking user inputs and variable initialization
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as a decimal: " ))
total_cost = float(input("Enter the cost of your dream home: "))
monthly_salary = annual_salary / 12
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04 # annual rate of return
months= 0
while current_savings < portion_down_payment :
    current_savings += (monthly_salary * portion_saved) + (current_savings * r / 12)
    months += 1
print("Number of months: " + str(months))

Part B 
# Taking user inputs and variable initialization
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as a decimal: " ))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise=float(input("Enter the semi-annual raise, as a decimal: " ))
monthly_salary = annual_salary / 12
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04 # annual rate of return
months= 0
while current_savings < portion_down_payment :
    if months >0 and months % 6 == 0:
        monthly_salary *=  (1 + semi_annual_raise)
    current_savings += (monthly_salary * portion_saved) + (current_savings * r / 12)
    months += 1
print("Number of months: " + str(months))


Part C
# Taking user inputs and variable initialization
annual_salary = float(input("Enter the starting salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
monthly_salary = annual_salary / 12
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04 # annual rate of return
no_of_months = 36
low = 0
high = 10000
guess_rate = int((high + low)/2)
steps = 0
# Initail test to check if the salary is sufficient
for i in range(1,no_of_months+1) :
    if i > 0 and i % 6 == 0:
        monthly_salary *=  (1 + semi_annual_raise)
    current_savings += monthly_salary + (current_savings * r / 12) 
if current_savings < portion_down_payment -100 :
        print("It is not possible to pay the down payment in three years")
else: # determine the best rate for savings
    while True :
        current_savings = 0
        monthly_salary = annual_salary / 12
        for i in range(1 , no_of_months + 1):
            if i >0 and i % 6 == 0:
                monthly_salary *=  (1 + semi_annual_raise)
            current_savings += (monthly_salary * guess_rate / 10000) + (current_savings * r / 12)
        steps += 1
        if current_savings < portion_down_payment - 100:
                low = guess_rate
                guess_rate = int((high + low)/2)
        elif current_savings > portion_down_payment + 100:
                high = guess_rate
                guess_rate = int((high + low)/2)
        elif current_savings >= portion_down_payment -100 and current_savings <= portion_down_payment +100 :
            print("Best saving rate: " + str(guess_rate/10000))
            print("Steps in bisection search: " + str(steps))
            break
"""
"""Section 2
# FIbonacci series
# Taking user input and variables initialization
n= int(input("Enter the number of elements: "))
first = 0
second = 1
update = first + second
series = 1
if n == 0 :
    print("invalid input")
for i in range(n-1) :
    series += update
    first = second
    second = update
    update = first + second
    
print(series)
"""

# Combination exercise
n=int(input("Enter the value of n: "))
