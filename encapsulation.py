class A:
    _a=10 #protected
    __b=20 #private
    
    def show(self):
        print("a=",self._a)
        print("b=",self.__b)
        
a=A()
a.show()
print("outside the value of a=",a._a)
print("outside the value of b=",a.__b)