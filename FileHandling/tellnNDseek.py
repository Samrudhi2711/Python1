f=open('E:\Python1\File Handling\data.txt','r')

#tell()
'''print(f.tell())
f.read(8)
print(f.tell())
f.close()'''

#seek()
print(f.tell())
f.read(8)
print(f.tell())
f.seek(0)
print(f.read())
f.close()
