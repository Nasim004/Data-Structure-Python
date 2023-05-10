

def Prime(num,i=2):
    if num == i:
        return num
    elif num%i == 0:
        return False
    return Prime(num,i+1)

num = 5
if Prime(num):
    print(num ,"is a prime number")
else:
    print(num ,"is not a prime number")
    


