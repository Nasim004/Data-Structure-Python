

def insertationSort(arr):

    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key


arr = [9, 5, 4, 3, 2, 1, 0]
insertationSort(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")
