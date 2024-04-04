class A:
    num1=int(input("Enter the 1st number="))
    num2=int(input("Enter the 2nd number="))
    
    def add(self):
        print("Addition of 2 number=",self.num1+self.num2)
        
    def sub(self):
        print("Subtraction of 2 number=",self.num1-self.num2)
        
class B(A):
    
    def mul(self):
        print("Multiplication of 2 number=",self.num1*self.num2)
        
    def div(self):
        print("Division of 2 number=",self.num1/self.num2)
        
obj=B()
obj.add()
obj.sub()
obj.mul()
obj.div()

    