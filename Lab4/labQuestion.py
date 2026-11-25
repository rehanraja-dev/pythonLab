''' WAP ti implement static method to validate email, class method to show total students '''

class Student:
    __total_students = 0

    def __init__(self, mail, name):
        self.__email = mail
        self.__name = name
        Student.__total_students += 1

    def showStudents(self):
        print(self.__name, self.__email)

    def retMail(self):
        return self.__email
    
    def retName(self):
        return self.__name
    
    @staticmethod
    def checkMail(mail):
        if "@" in mail and "." in mail and mail.count("@") == 1:
            return True
        return False
    
    @staticmethod
    def checkName(name:str):
        if name.isnumeric():
            return False
        return True

    @classmethod
    def totalStudents(cls):
        print(f"Total students: {cls.__total_students}")

s1 = Student("rehan@gmail.com", "rehan")
if Student.checkMail(s1.retMail()) and Student.checkName(s1.retName()):
    print(s1.showStudents())
Student.totalStudents()