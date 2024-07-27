a=10
def sam_fun1():
    b=40
    print("Local variable:",b)
    print("global variable:",a)
def sam_fun2():
    c=20
    print("local variable:",c)
    print("global variable:",a)
    
sam_fun1()
sam_fun2()
