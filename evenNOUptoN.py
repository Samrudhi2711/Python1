'''1. Write a program to accept an integer n and display all even numbers upto n.'''
n=int(input("Enter the number="))
for i in range(n):
    if i%2==0:
        print(i)