class Student:
     def __init__(self, studentName, enrolled):
         self.studentName = studentName
         self.GPA = 0.0
         self.creditHours = 0
         self.enrolled = enrolled
         self.classes = []
         
newStudent = Student ("Venus de Milo",False)
print (newStudent.creditHours)

#number.py
class Number :
    def __init__(self,value=0,even=True):
        self.value = value
        self.even = even
        
number_instance = Number(101,False)
