def lefrotate(arr, n, d):
    for i in range(d):
       lefrotatebyone(arr,n)
       i = i +1

def lefrotatebyone(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def printarray(arr, size):
    for i in range(size):
        print("%d"% arr[i],end=" ")

num = int(input("Enter the length of the array: "))

lst = []

for i in range(num):
    ele = int(input())
    
    lst.append(ele)

rotator = int(input("Enter the number of places you want to rotate: "))

lefrotate(lst, num, rotator)
printarray(lst, num)