num = int(input("Enter the number: "))

if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i ) == 0:
            print("{} is not a prime number".format(num))
            break
    else:
         print("{} is a prime number".format(num))
            
else:
    print(num, "is not a prime number.")

