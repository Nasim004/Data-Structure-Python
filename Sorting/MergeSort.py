

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        l = arr[:mid]
        r=arr[mid:]
        mergeSort(l)
        mergeSort(r)

        i=k=j=0

        while i <len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k]=l[i]
                i = i+1
            else:
                arr[k] = r[j]
                j=j+1
            k=k+1

        while i < len(l):
            arr[k]=l[i]
            k=k+1
            i=i+1
        while j < len(r):
            arr[k]=l[j]
            k+=1
            i+=1
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()      
          

arr = [5,4,3,2,-1,-4,-7]
mergeSort(arr)
printList(arr)