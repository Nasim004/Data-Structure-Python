def partiton(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j]<= pivot:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1
def qucikSort(arr,low,high):
    if low < high:
        pi = partiton(arr,low,high)
        qucikSort(arr,low,pi-1)
        qucikSort(arr,pi+1,high)

arr = [9,8,7,6,5]

qucikSort(arr,0,len(arr)-1)
print(f'Sorted Array : {arr}')