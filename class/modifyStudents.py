class student:
    def __init__(self, enrollNo, sName, branch, marks, per):
        self.__enrollNo = enrollNo
        self.__sName = sName
        self.__branch = branch
        self.__marks = marks
        self.__per = per

    def showStudent(self):
        print(f"Student Name: {self.__sName}\n Marks: {self.__marks}\n Branch: {self.__branch} \n EnrollNo: {self.__enrollNo}\n Percentage: {self.__per}")

    def modifyStudent(self, sName, enrollNo, branch, marks, per):
        self.__enrollNo = enrollNo
        self.__sName = sName
        self.__branch = branch
        self.__marks = marks
        self.__per = per

    # Added getter to access the private enrollNo from outside the class
    def getEnrollNo(self):
        return self.__enrollNo
 

students = []
for i in range(2):
    print(f"\nEntering details for Student {i+1}:")
    name = input("Enter Name: ")
    enrollNo = int(input("Enter EnrollNo: "))
    branch = input("Enter Branch: ")
    marks = int(input("Enter Marks: "))
    per = float(input("Enter Percentage: "))

    st = student(enrollNo, name, branch, marks, per)
    students.append(st)


print("\n--- Modify Student Details ---")
search_enroll = int(input("Enter the EnrollNo of the student you want to modify: "))

# Search loop
found_student = None
for st in students:
    if st.getEnrollNo() == search_enroll:
        found_student = st
        break

if found_student:
    print("\nStudent Record Found! Enter the new details:")
    new_name = input("Enter New Name: ")
    new_enrollNo = int(input("Enter New EnrollNo: "))
    new_branch = input("Enter New Branch: ")
    new_marks = int(input("Enter New Marks: "))
    new_per = float(input("Enter New Percentage: "))
    
    found_student.modifyStudent(new_name, new_enrollNo, new_branch, new_marks, new_per)
    print("\nStudent record modified successfully!")
else:
    print("\nError: Student with this Enrollment Number not found.")


print("\n--- Updated Student List ---")
for st in students:
    st.showStudent()
    print("-" * 20)
