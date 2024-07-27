def get_factorial(num):
    f=1
    i=1
    while i<=num:
        f=f*i
        i=i+1
    return f
f1=get_factorial(5)
print("Factorial of 5 is:",f1)
