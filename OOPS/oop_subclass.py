class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initialized SchoolMember:", self.name, self.age)
        
    def display(self):
        print("Name:", self.name) 
        print("Age:", self.age)
        
class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        self.salary = salary
        super().__init__(name, age)
        print("Initialized Teacher:", self.name, self.age, self.salary)
    
    def tell(self):
        SchoolMember.tell(self)
        print("Salary:", self.salary)
        
        
class Student(SchoolMember):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
        print("Initialized Student:", self.name, self.age, self.marks)
        
    def tell(self):
        SchoolMember.tell(self)
        print("Marks:", self.marks)

t = Teacher("Mr. Smith", 40, 50000)
s = Student("Alice", 20, 90)

members = [t, s]
for member in members:
    member.display()
    member.tell()