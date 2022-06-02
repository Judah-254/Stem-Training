class person:
    def __init__(self,name,Date_of_birth,height,weight):
        self.name=name
        self.Date_of_Birth=Date_of_birth
        self.height=height
        self.weight=weight
    def details(self):
        print(f"My name is {self.name},my D.O.B is {self.Date_of_Birth},my height is {self.height} and my weight is {self.weight}")
    def 
p1=person("Judah",18,"75ft","63kg")
p1.details()
class Student(person):
    def __init__(self,name,Class,Fav_subject):
        super().__init__(name,Class,Fav_subject,weight=63)
        self.Class=Class
        self.Fav_subject=Fav_subject
    def details(self):
        print(f"my class is {self.Class} and my Favourite subject is {self.Fav_subject}")
S1=Student("Judah","Grade 5","History")
S1.details()
class Teacher(person):
    def __init__(self,name,Teaching_subject,salary):
        super().__init__(name,Teaching_subject,salary,weight=97)
        self.Teaching_subject=Teaching_subject
        self.salary=salary
    def details(self):
        print(f"I am {self.name} I teach {self.Teaching_subject} and I earn {self.salary}")
T1=Teacher("Mwalimu_Andrew","Biology",55000)
T1.details()
