""" Group 7 (Alpha) """
""" Section 2 - B """
#Number of combinations of n objects taken r 
n=int(input("Enter value for n: "))
r=int(input("Enter value for r: "))
k=n-r
fact_n=1  #Initialize a variable "fact_n" 
fact_r=1  #Initialize a variable "fact_r"
fact_k=1  #Initialize a variable "fact_k"
for i in range(1,n+1):
    fact_n*=i
for j in range(1,r+1):
    fact_r*=j
for l in range(1,k+1):
    fact_k*=l
print("The number of combinations of n objects taken r is",fact_n/(fact_r*fact_k))

