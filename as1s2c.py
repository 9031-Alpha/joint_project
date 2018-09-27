""" Group 7 (Alpha) """
""" Section 2 - C """
# Binomial sum
# Taking user input and initializing variables
x=int(input("Enter the value of x: "))
n=int(input("Enter the value of n: "))
a=int(input("Enter the value of a: "))
bina=0
for k in range(0, n+1):
    r = n-k
    fact_n = 1
    for i in range(1,n+1):
        fact_n*=i
    fact_k = 1
    for j in range(1,k+1):
        fact_k *= j
    fact_r = 1
    for l in range(1,r+1):
        fact_r *= l
    bina += (fact_n / (fact_k * fact_r)) * x**k * a**(n-k)
print(bina)

