
def unique(arr):

    dict = {}

    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for i in arr:
        if dict[i] == 1:
            return i

    return 0


arr = [1, 1, 2, 2, 3, 4, 5, 5]
unique_element = unique(arr)
print(unique_element)
