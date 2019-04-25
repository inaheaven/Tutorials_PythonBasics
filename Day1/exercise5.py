class Calc:
    def __init__(self):
        self.result =0

    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calc()
cal2 = Calc()


class Employee:
    empCount = 0

    #생성자
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("total emplyoee number  %d" % Employee.empCount)

    def displayEmployee(self):
        print("employee: %s" % self.name, ", Salary: %s" % self.salary )

    #소멸자
    # __ 로 시작하면 내부 함수
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")

emp1 = Employee("kim", 3000)
emp1.displayCount()
emp1.displayEmployee()

emp2 = Employee("park", 4000)
emp2.displayCount()
emp2.displayEmployee()

emp3 = Employee("lee", 500)
emp3.displayCount()
emp3.displayEmployee()

emp4 = Employee("shin", 20)
emp4.displayCount()
emp4.displayEmployee()

del emp1

emp3.displayCount()

class Parent:
    parentAttr = 100
    def __init__(self):
        print("CALL PARENT CONSTRUCTOR")
    def parentMethod(self):
        print("call parent method")
    def setAttr(self, attr):
       Parent.parentAttr = attr
    def getAttr(self):
        print("Parent attr", Parent.parentAttr)

#inherits
class Child(Parent):
    def __init__(self):
        print("call child constructor")
    def childMethod(self):
        print("call child method")
    def getAttr(self):
        print("child attr", Child.parentAttr)

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(300)
c.getAttr()