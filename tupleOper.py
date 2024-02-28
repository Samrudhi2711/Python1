#Finding length using __len__ fun 
tuple1=(10,20,30,40,"sam",90.344,56)
a=tuple1.__len__()
print("tuple1 has",a,"element")

#membership operator
tuple=(10,20,30,40,"sam",90.344,56,45,45.34,90.54,45656,44444,1111111,222222,)
print("Element 10 present in tuple",10 in tuple)
print("Element 40 present in tuple",40 not in tuple)
print("Element 344 present in tuple",344 in tuple)
print("Element 44444 present in tuple",44444 not in tuple)


#concatenation of tuple
tuple2=(10,20,30,40,"sam","sal")
tuple3=(10,20,30,"samru","saloni")
tuple4=tuple2+tuple3
print("Concat 2 tuples:",tuple4)

#multiplying of tuple
tuple2=(10,20,30,40,"sam","sal")
tuple5=tuple2*3
print("tuple2 multipy by 3 :",tuple5)


