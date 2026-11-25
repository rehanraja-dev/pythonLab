class Student:
    def __init__(self,m,p,c):
        self.math = m 
        self.physics = p 
        self.chemistry = c

    def average(self):
        avg = self.math + self.physics + self.chemistry
        print(f"Average marks: {avg}")

s = Student(1,2,3)
s.average()
