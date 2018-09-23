#Taking user inputs and initializing variables
annual_salary=float(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost=float(input("Enter the cost of your dream home: "))
semi_annual_raise=float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment=total_cost*0.25
current_savings=0.0
r=0.04
monthly_salary=annual_salary/12
number_of_months=0

while (current_savings<portion_down_payment):
    current_savings += (current_savings*r/12) + monthly_salary*portion_saved
    number_of_months = number_of_months+1
    if (number_of_months%6==0):
        monthly_salary+=monthly_salary*semi_annual_raise

print("Number of months: " + str(number_of_months))
