def compund_interest(p, t, r):
    ci = p * pow((1 + r/100), t)
    return ci

p = float(input("Enter the principal amount: "))
t = float(input("\nEnter the time period: "))
r = float(input("\nEnter the rate of interest: "))

print("Compound interest is ", compund_interest(p, t, r))

