def linearSearch(array,x,n):
    for i in range(0,n):
        if (array[i] == x):
            return i
    return -1

        
array = [1,4,2,1,4,21,5,32,0]
x=21
n=len(array)
result = linearSearch(array,x,n)
if (result == -1):
    print("Not Found")
else:
    print(result)