#append
list=[10,20,30,40,50,60,70,809,90]
print("original list")
print(list)

#append
list.append(600)
print("append 600")
print(list)

#insert
list.insert(4,"sam")
print("after adding sam.. at index 4")
print(list)

#extend
list2=[20,30,40,50]
list3=[1,2,3]
list2.extend(list3)
print("list2 extend list 3")
print(list2)


