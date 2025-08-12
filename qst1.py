#write a python program to create a class named students with attributes name,age,and grade.instantiate three student objects and display their attributes
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")



student1 = Student("tulsi", 20, "A")
student2 = Student("Sandeep", 21, "B")
student3 = Student("Ayush", 19, "A+")

print("Student Details:")
student1.display()
student2.display()
student3.display()
