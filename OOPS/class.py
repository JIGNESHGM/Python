class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        
# Creating an object of the student class   
s = student("Jignesh", 101)
# Accessing the attributes and methods of the object
s.display()
print("Name:", s.name)
print("Roll No:", s.rollno)
