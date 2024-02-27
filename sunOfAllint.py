'''   2. Accept two integers x and y and calculate the sum of all integers between x and y (both 
inclusive)'''
n1=int(input("Enter the value of n1="))
n2=int(input("Enter the value of n2="))
sum=0
for i in range (n1,n2+1):
    sum=sum+i
print("Sum of all number=",sum)