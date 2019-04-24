class Student:
    studentName = ""
    __stuAge = 20

    def __init__(self):
        print("call student constructor")

    def gotoSchool(self, name, age):
        self.studentName = name
        self.__stuAge = age
        print(self.studentName, self.__stuAge)

    def gotoSchool(self):
        print("call student goto school")

    def __del__(self):
        print("call student destructor")


class MiddleStudent(Student):

    def __init__(self):
        print("call midstu constructor")



stu = Student()
stu.gotoSchool("lee", 34)
stu2 = MiddleStudent()
stu2.gotoSchool()
stu2.gotoSchool("park", 34)
