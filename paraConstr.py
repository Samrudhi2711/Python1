class employee:
    company_name="ABC Company"
    
    def __init__(self, Ename,Esalary):
        self.Ename=Ename
        self.Esalary=Esalary
        
    def welcome(self):
        print("welcome to company",self.Ename)
        
    def get_salary(self):
        return self.Esalary
    
obj=employee("Sai",30000)
obj.welcome()
print("salary of employee",obj.get_salary())