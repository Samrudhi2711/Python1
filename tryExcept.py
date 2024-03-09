list=[10,20,30,40,506,60,70,80]
try:
    print("Second element:",list[1])
    print("third element:",list[3])
    print("9th element:",list[9])
except IndexError:
    print("Index error occure:")
    
