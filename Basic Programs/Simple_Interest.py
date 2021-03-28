def Simple_Interest(p, t, r):
    si = (p*t*r) / 100
    return si

p = float(input("Enter the prinicipal amount: "))
t = float(input("Enter the time period: "))
r = float(input("Enter the rate of interest: "))

print("Simple interest is ", Simple_Interest(p, t, r))
