class student:
    def __init__(self, enrollNo, sName, branch, marks, per):
        self.__enrollNo = enrollNo
        self.__sName = sName
        self.__branch = branch
        self.__marks = marks
        self.__per = per

    def showStudent(self):
        print(f"Student Name: {self.__sName}\n Marks: {self.__marks}\n Branch: {self.__branch} \n EnrollNo: {self.__enrollNo}\n Percentage: {self.__per}")


students = []
for i in range(2):
    name = input("Enter Name: ")
    enrollNo = int(input("Enter EnrollNo: "))
    branch = input("Enter Branch: ")
    marks = int(input("Enter Marks: "))
    per = float(input("Enter Percentage: "))

    st = student(enrollNo, name, branch, marks, per)
    students.append(st)

for st in students:
    st.showStudent()