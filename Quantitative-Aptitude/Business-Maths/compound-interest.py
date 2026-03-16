#compound interest calculator

principal = float(input("Enter principal amount "))
interest = float(input("Enter interest rate as percentage "))
time = float(input("Enter number of years "))
conversion = float(input("Enter number of times compounded per year "))

real_interest = interest/(conversion * 100)
real_time = time * conversion


def compound(p,i,n):
    a = p * ((1 + i) ** n)
    return a
print(f"The total amount after {time} years is {compound(principal,real_interest,real_time)}")
print(f"The compound interest earned is {compound(principal,real_interest,real_time)-principal}")
