class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(f"My name is {self.name} and my age is {self.age}")
p1=person("Judah",18)
p1.details()
class Employee(person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def details(self):
        print(f"My name is {self.name} and my age is {self.age}my salary is{self.salary}")
p2=Employee("Judah",18,500000)
p2.details()