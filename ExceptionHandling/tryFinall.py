try:
    l=[1,2,3,4,5]
    i=int(input("Enter the index:"))
    print(l[i])
except:
    print("some error occured")
finally:
    print("I am always executed")
