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

    def email(self):
        return self.fullname() + '@gmail.com'

    def __add__(self, other): # operator overloading
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    def __repr__(self) -> str:
        return f'Employee({self.first}, {self.last}, {self.pay})'


emp1 = Employee('Eric', 'Pattinson', 500000)
emp2 = Employee('Kim So', 'Yong', 450000)

print(emp1 + emp2) # + = int.__add__(emp1, emp2)
print(len(emp1))
print(repr(emp1))

# ပုံမှန်အားဖြင့်ဆို add, len, repr တို့က ကိုယ်ဆောက်ထားတဲ့ obj တွေမှာခေါ်သုံးလို့မရဘူး 
# သုံးလို့ရအောင် magic method တွေထည့်ရေးရတယ် 