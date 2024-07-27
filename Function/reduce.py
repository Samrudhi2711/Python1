from functools import reduce
no=[10,20,30,40,50,60,70,80]

def mysum(x,y):
    return x+y
sum=reduce(mysum,no)
print(sum)
