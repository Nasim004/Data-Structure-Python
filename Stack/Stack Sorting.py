def stackSort(s):
    if not s:
        return 
    x = s.pop()
    stackSort(s)
    tempStack = []
    while s and s[-1] > x:
        tempStack.append(s.pop())
    s.append(x)
    while tempStack:
        s.append(tempStack.pop())
        
s = []
s.append(32)
s.append(2)
s.append(122)
s.append(12)
s.append(0)
stackSort(s)

while s:
    print(s.pop(),end=" ")