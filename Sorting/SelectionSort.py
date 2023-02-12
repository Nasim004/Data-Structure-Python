arr = [5,4,3,2,1]
for i in range(len(arr)):
    min_index = i
    n= len(arr)
    for j in range(i+1,n):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]
for i in range(len(arr)):
    print("%d " %arr[i],end="") 