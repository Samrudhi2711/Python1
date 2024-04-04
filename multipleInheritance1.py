class saloni:
    back="MySQL DB and Java"
    def Backend(self):
        print("Backend Task Implemented using =",self.back)
class komal:
    front="HtML CsS and JS"
    def frontend(self):
        print("Frontend task Implementeed using",self.front)
        
class TeamLead(saloni,komal):
    def show(self):
        print("Dynamic webpage created")
        
        
obj=TeamLead()
obj.Backend()
obj.frontend()
obj.show()