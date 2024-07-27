def cube(x):
    return x*x*x
print(cube(6))
l=[1,2,3,4,5,6,7,8,9]
# new=list(map(cube,l))
# print(new)


#using lambda function 
new1=list(map(lambda x: x*x,l))
print(new1)
