import random
n = 10
#arr = [random.randint(0, 100) for i in range(n)]
arr = [95, 61, 70, 100, 77, 48, 78, 76, 43, 59]
print arr 

low = 0
high = n - 1
while(low < high):
    if arr[low] % 2 == 1:
        low += 1
        continue
    
    if arr[high] % 2 == 0:
        high -= 1
        continue
    
    tmp = arr[high]
    arr[high] = arr[low]
    arr[low] = tmp
    high -= 1
    low += 1
    
print arr
