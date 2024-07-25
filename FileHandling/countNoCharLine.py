f=open('E:\Python1\File Handling\data.txt','r')
N_of_words=0
N_of_Lines=0
N_of_char=0
for line in f:
    N_of_Lines+=1
    
    line=line.strip("\n")
    N_of_char+=len(line)
    
    list=line.split()
    N_of_words+=len(list)
    
f.close()
print("No of lines in file =",N_of_Lines)
print("No of character in file=",N_of_char)
print("NO of words in file =",N_of_words)