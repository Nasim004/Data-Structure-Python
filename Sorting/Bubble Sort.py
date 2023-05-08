

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [4, 32, 41, 312, 4, 1, 0]
bubbleSort(arr)


for i in range(len(arr)):
    print(arr[i], end=" ")
