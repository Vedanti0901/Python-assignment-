parent class 1
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show_person(self):
        print("name : ",self.name)
        print("age : ",self.age)
        
class Employee(person):
    def __init__(self, name, age,employee_id,salary):
        person.__init__(self,name,age)
        self.employee_id = employee_id
        self.salary = salary
    def show__employee(self):
        print("Employee: " ,self.employee_id)
        print("salary: ",self.salary)
  
class manager(Employee,person):   
    def __init__(self, name, age, employee_id, salary,department):
        Employee.__init__(self,name,age,employee_id, salary)
        self.deparment= department
    def show_manager(self):
        print("department: ", self.deparment)
        
m =manager("kronnik",18,101, 50000, "IT")

m.show_person()
m.show__employee()
m.show_manager()
         
            
        
        
              