class Student:
    def __init__(self):
        self.studentName = ""
        self.GPA = 0.0
        self.creditHours = 0
        self.enrolled = True
        self.classes = []
        
newStudent = Student()
newStudent.studentName = "George P. Burdell"
newStudent.enrolled = True
newStudent.GPA = 3.9
newStudent.creditHours = 1334
newStudent.classes = ["CS1301", "PHYS3001", "ISYE3029"]

#number.py
class Number :
    def __init__(self):
        self.value = 0
        self.even = True
        
number_instance = Number()
number_instance.value = 101
number_instance.even = False