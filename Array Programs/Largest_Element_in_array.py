def Largest(arr, n):
    max = arr[0]

    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    return max

lst = []
num = int(input("Enter the number of the elements in the array: "))

for i in range(0,num):
    ele = int(input())

    lst.append(ele)

print("Largest number in the array is : ", Largest(lst, num) )


