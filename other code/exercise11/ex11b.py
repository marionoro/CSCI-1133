class Person:
    def __init__(self, name='', address ='', phonenum = '', email =''):
        self.name = name
        self.address = address
        self.phonenum = phonenum
        self.email = email
    def __repr__(self):
        return 'Person, ' + self.name

class Student(Person):
    def __init__(self, grade=''):
        super().__init__()
        self.grade = grade
    def __repr__(self):
        return 'Student, ' + self.name

class Employee(Person):
    def __init__(self, office='', salary='', hiredate=''):
        super().__init__()
        self.office = office
        self.salary = salary
        self.hiredate = hiredate
    def __repr__(self):
        return 'Employee, ' + self.name

class Faculty(Employee):
    def __init__(self, officehrs='', rank=''):
        super().__init__()
        self.officehrs = officehrs
        self.rank = rank
    def __repr__(self):
        return 'Faculty, ' + self.name

class Staff(Employee):
    def __init__(self, title=''):
        super().__init__()
        self.title = title
    def __repr__(self):
        return 'Staff, ' + self.name

def main():
    list1 = [Person('Aaron')]
    list2 = [Student(), Employee(), Faculty(), Staff()]
    list3 = ['Bob', 'Cassie', 'Damian', 'Erik']
    for i in range(4):
        a = list2[i]
        a.name = list3[i]
        list1.append(a)
    for j in range(5):
        print (list1[j])
