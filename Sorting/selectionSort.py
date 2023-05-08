

def selectionSort(arr):

    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                arr[min_index], arr[j] = arr[j], arr[min_index]


arr = [6, 4, 3, 2, 1, 5]
selectionSort(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")
