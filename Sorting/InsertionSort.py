arr = [5,4,3,2,1]

for i in range(len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = key
    
for i in range(len(arr)):
    print("%d " % arr[i],end="")