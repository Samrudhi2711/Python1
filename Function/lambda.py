
# def double(x):
#     return x*x

#show the cube of the number
cube=lambda x:x*x*x
print(cube(5))

double=lambda x:x*2
print(double(4))

#calculate the average
avg=lambda x,y,z:(x+y+z)/3
print(avg(4,5,6))

#passing lamabda to the function
def app(fx,value):
    return 6+fx(value)

print(app(lambda x:x*x*x,2))



