class father:
    surname="Gadge"
class son(father):
    def show(self):
        print("Samrudhi",self.surname)
        
class Gson(son):
    def desp(self):
        print("Saloni",self.surname)
        
obj=Gson()
obj.show()
obj.desp()