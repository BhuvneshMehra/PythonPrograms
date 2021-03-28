start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for i in range(start, end + 1):
    if i>1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            print(i)
