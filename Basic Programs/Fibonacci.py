#Method 1: Using Recursion
def Fibonacci(n):
    if n<0:
        print("Wrong Input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

num = int(input("Enter the sequence number in Fiboanacci series: "))
for i in range(1,num):
    print(Fibonacci(i), "\n")

#Method 2: Using Dynamic Programming.
