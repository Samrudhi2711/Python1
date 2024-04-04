class father:
    surname="Gadge"
    def show(self):
        print("My surname is",self.surname)
class son(father):
    def disp(self):
        print("My name is samrudhi and my surname is",self.surname)

class son1(father):
    def disp1(self):
        print("My name is prachi and my surname is",self.surname)
        
s1=son1()
s1.show()
s1.disp1()

s2=son()
s2.disp()
s2.show()
        