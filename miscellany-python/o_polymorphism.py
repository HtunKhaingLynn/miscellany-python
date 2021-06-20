# Polymorphism class method
class  CompanyA:
    def employee(self):
        print('Need a programmer')
        print('Level C')

class  CompanyB:
    def employee(self):
        print('Need a hacker')
        print('Level A')

class  CompanyC:
    def employee(self):
        print('Need a scientist')
        print('Level A')

class People:
    def fun(self, obj):
        obj.employee()

comA = CompanyA()
comB = CompanyB()
comC = CompanyC()
people = People()
people.fun(comA)
comList = [comA, comB, comC]
for obj in comList:
    people.fun(obj)
