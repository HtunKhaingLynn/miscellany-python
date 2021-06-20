from datetime import date

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

    def total_salary(self):
        self.pay += self.bonus
        return self.pay
    
    def fullname(self):
        return f'{self.first} {self.last}'

    @classmethod
    def from_string(cls, str):
        first, last, pay = str.split('-')
        pay = int(pay)
        return cls(first, last, int(pay))

    @staticmethod
    def work_day(date): # same as util func
        if date == 0 or date == 6:
            return False
        return True

    def set_date(self):
        today = date.today().weekday()
        return self.work_day(today)

emp1 = Employee('Eric', 'Pattinson', 500000)
emp2 = Employee('Kim So', 'Yong', 450000)
emp3 = Employee.from_string('Eric-Pattinson-900000')
print(emp3.set_date())
print(emp3.total_salary())