import math
def IsPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def IsFibonacci(x):
    return IsPerfectSquare(5*x*x + 4) or IsPerfectSquare(5*x*x - 4)

num = int(input("Enter the number upto you want to check"))

for i in range(1,num):
    if IsFibonacci(i) == True:
        print(i , "is a Fibonacci number.")
    else:
        print(i , "is not a Fibonacci number.")