def filter_fun(x):
    return x>2
l=[1,2,3,4,5,6,7,8,9]
new=list(filter(filter_fun,l))
print(new)

#using lamabda function
l1=[10,29,39,48,576,7]
new1=list(filter(lambda x:x>40,l1))
print(new1)
 
