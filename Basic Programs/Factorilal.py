
#Method 1: Recursive

def factorial(n):
    return 1 if(n==1 or n==0) else n * factorial(n-1);

num = int(input("Enter the number: "))

print("Factorial of {0} is {1}".format(num, factorial(num)))

'''
#Method 2: Iterative

def factorial (n):
    if n < 0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact = 1 
        while (n>1):
            fact *= n
            n -= 1
        return fact


num = int(input("Enter the number: "))

print("Factorial of {0} is {1}".format(num, factorial(num)))
'''