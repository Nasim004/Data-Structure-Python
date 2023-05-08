

def checking(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
    if len(stack) == 0:
        return True
    return False


a=checking('()()()')
print(a)
