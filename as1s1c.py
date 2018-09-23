#Taking user inputs and initializing variables
starting_salary=float(input("Enter the starting salary: "))
total_cost=1000000
semi_annual_raise=0.07
portion_down_payment=total_cost*0.25
r=0.04
number_of_months=36
current_savings=0.0
current_savings_low_income=0.0
left=steps=0
right=10000
mid=(left+right)/2
monthly_salary=starting_salary/12

#Check if the starting salary is not enough to pay for the down payment in 3 years
for i in range (1, number_of_months+1):
    current_savings_low_income += (current_savings*r/12) + monthly_salary
    if i%6==0:
        monthly_salary+=monthly_salary*semi_annual_raise

if current_savings_low_income<portion_down_payment-100:
    print("It is not possible to pay the down payment in three years.")
else:
    while (current_savings<portion_down_payment-100 or current_savings>portion_down_payment+100):
        monthly_salary=starting_salary/12
        current_savings=0.0
        steps+=1
        for i in range (1, number_of_months+1):
            current_savings += (current_savings*r/12) + monthly_salary*int(mid)/10000.0
            if i%6==0:
                monthly_salary+=monthly_salary*semi_annual_raise
        if current_savings<portion_down_payment-100:
            left=mid+1
        elif current_savings>portion_down_payment+100:
            right=mid-1
        mid=(left+right)/2
    
    print("Best savings rate: " + str(int(mid)/10000.0))
    print("Steps in bisection search: " + str(steps))