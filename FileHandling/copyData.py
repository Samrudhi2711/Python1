f1=open("E:\Python1\File Handling\first.txt",'r')
f2=open("E:\Python1\File Handling\second.txt ",'w')
data=f1.readlines()
for line in data:
    f2.write(line)
print(f2.readlines())
f1.close()
f2.close()