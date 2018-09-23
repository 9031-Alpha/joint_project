

""" Assignment 1: Alpha Group (7) """

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


""" Part B """
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

""" Part C """
