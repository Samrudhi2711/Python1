
list=['P','Y','T','H','O','N','P','R','O','G','R','A','M','M','I','N','G']
print("print original string")
print(list)

#del
del list[2]
print("After deleting index 2 value  T ")
print(list)

del list[2:5]
print("After deleting 2:5 rang ")
print(list)

'''del list
print(list)'''

list2=[10,20,30,40,50,60,70,70,70,70,70,70,80,90]
list2.remove(30)
print("After deleting 30")
print(list2)

'''list2.pop(5)
print("after remove index 5 value")
print(list2)'''

#list2.clear()
#print(list2)

#membership operation
print("presence of 10 in list is:",10 in list2)
print("presence of1000 in list",1000 in list2)
print("absence of 60 in list2",60 not in list2)

b=list2.count(70)
print("count=",b)

list2.sort()
print("sort",list2)

list2.reverse()
print("reverse",list2)



