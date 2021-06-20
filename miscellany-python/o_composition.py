# Code reuse လူပ်ချင်ရင်composition ကိုသုံးပါ။ 
# ဘာလို့လဲဆိုတော့ inheritance hierarchicy များလာတာနဲ.အမျှ classes တွေဟာ dependency များလာပါတယ်။ 
# Base class တစ်ခုကိုလိုက်ပြောင်းတာနဲ့အောက်က child classes တွေမှာပါ effect ဖြစ်နိုင်ပါတယ်။ 
# Composition ဆိုတာက ကိုယ်သုံးလိုတဲ့ class ကို reference variable သုံးပြီးယူသုံးတာပါ --> Author: Thet Khine

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus

class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.salary_obj = Salary(pay, bonus) 

    def total_salary(self):
        return self.salary_obj.annual_salary()

employee = Employee('AkoHtun', 20, 500000, 200000)
print(employee.total_salary())

        