
#Method 1: Using If-Else statement
def maximum(a,b):
    if(a>=b):
        return a
    else:
        return b

num1 = int(input("Enter the first number:"))
num2 = int(input("\nEnter the second number:"))

print("Maximum of {0} and {1} is {2}.".format(num1 , num2, maximum(num1,num2) ))

'''
#Method 2: Using the Max Function


num1 = int(input("Enter the first number:"))
num2 = int(input("\nEnter the second number:"))

print("Maximum of {0} and {1} is {2}.".format(num1 , num2, max(num1,num2) ))
'''