class Employee:

    # class variables 
    bonus = 10000
    no_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + self.last + '@gmail.com'
        # add 1 to no_of_emps every time we create an instance 
        Employee.no_of_emps += 1 # call class variables(u can use 'self' too)

    @property # use to call method like an attribute
    def total_salary(self):
        self.pay += self.bonus
        return self.pay
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.getter
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.deleter
    def fullname(self):
        print('Name is deleted')
        self.first = None
        self.last = None

    def email(self):
        return self.fullname() + '@gmail.com'


emp1 = Employee('Eric', 'Pattinson', 500000)
emp2 = Employee('Kim So', 'Yong', 450000)
emp1.fullname = 'Ako Htun' # setter

print(emp1.total_salary)
print(emp1.fullname) # getter
del emp1.fullname # deleter
print(emp1.fullname)