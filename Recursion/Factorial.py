
def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
n = int(input("Enter the number "))

if n < 0:
    print("No factorial for negative number")
elif n == 0:
    print("prime is 1")
else:
    print("the factorial of ", n, "is", factorial(n))
