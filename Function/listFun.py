def show_list_element(a):
    print("List Container")
    i=0
    while i<a.__len__():
        print("At index",i,"element is",a[i])
        i=i+1
ls1=[10,20,30,40,50,60]
ls2=[1,2,3,4,5,6]

show_list_element(ls1)
show_list_element(ls2)
