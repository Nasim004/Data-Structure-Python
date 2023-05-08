
def largest(arr):

    n = len(arr)

    if n < 3:

        print("Array donot have 3 elements")

    else:
        first = arr[0]
        second = arr[1]
        third = arr[2]

        for i in range(3, n):
            if arr[i] > third:
                if arr[i] > second:
                    if arr[i] > first:
                        third = second
                        second = first
                        first = arr[i]
                    else:
                        third = second
                        second = arr[i]
                else:
                    third = arr[i]
        return third


arr = [1, 2, 3, 4, 5, 6]

third_largest = largest(arr)
print(third_largest)
