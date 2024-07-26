#set union
A={1,2,3,4,5}
B={4,5,6,7,8}
C=A|B #A.union(B)
print("Set contain a:",A)
print("Set contain b:",B)
print("The Union operation result:",C)

#set intersection

A={1,2,3,4,5}
B={4,5,6,7,8}
C=A&B #A.intersection(B)
print("Set contain a:",A)
print("Set contain b:",B)
print("The intersection operation result:",C)

#set difference
A={1,2,3,4,5}
B={4,5,6,7,8}
C=A-B #A.difference(B) #unique value are display in set A
D=B-A #B.difference(A) #unique value are display in set B
print("Set contain a:",A)
print("Set contain b:",B)
print("a-b result:",C)
print("b-a result:",D)

#set symmetric_difference    display all value without similar 
A={1,2,3,4,5}
B={4,5,6,7,8}
e=A ^ B
print("Symmetric_difference result is=",e)


