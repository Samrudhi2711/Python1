f=open(r'E:\Python1\File Handling\data.txt')
#if f:
#   print("file sucessfuly opened")

'''data=f.read()
print(data)
f.close()'''

#read number of char in file

'''data=f.read(15)
print(data)
f.close()'''

#using readline()
'''data=f.readline()
data1=f.readline()
print(data)
print(data1)
f.close()'''

#using readlines()
'''data=f.readlines()
print(data)
f.close()'''

#using for loop
data=f.readlines()
for lines in data:
    print(lines,end="")
    f.close()
    
