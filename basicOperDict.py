#update(),__len__(),Assignment operator =

dict={1:"sam",2:"sal",3:"prachi",4:"yogesh",5:"vaishu",6:"samrudhi",7:"sid"}
print("Initial Dictionary content:",dict)

dict.update({"9":"sanika"})
print("update dict =",dict)

dict.update({"komal":"13/11/2004"})
print("After add komal value:",dict)

l=dict.__len__()
print("total length of the dictionary:",l)

dict1={1:10,2:20,3:30}
print("Initially dictionary content:",dict1)

dict1[2]=1000
print("After aupdate the key 2 value:",dict1)

#remove(), pop(), clear(),popithem()

del dict1[1]
print("After delete key 1",dict1)

# dict1.pop[2]
# print("After delete key 2",dict1)

dict1.popitem()
print("after using the popitem :",dict1)

dict1.clear()
print("after using the clear function")