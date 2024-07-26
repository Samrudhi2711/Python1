set1={10,20,30,40}
for i in set1:
    print(i)
    
#basic set operation
#update(),add(),len() remove(),pop(),clear(),remove()discard()

set2={3,4}
print("Initial set contain",set2)

set2.add(2)
print("After adding 2 in set2   :",set2)

set2.update([5,6,7])
print("After updating  list to it set contaion",set2)

set2.update([4,5],{1,6,8})
print("After adding another list and set contain",set2) 

#finding length
a=set2.__len__()
print("Length of set 2=",a)

set2.discard(2)
print("After discard 2 on the set=",set2)

set2.remove(8)
print("After removing 8 in the set:",set2)

set2.clear()

# set2.pop()
# print("pop one element in the list:",set2)
