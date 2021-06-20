from datetime import date
# from time import process_time 

# class Person:

#     no_of_person = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Person.no_of_person += 1

#     @classmethod # alternative constructor
#     def from_birth_year(cls, name, birth_year):
#         return cls(name, date.today().year - birth_year) # return a class object

#     def display(self):
#         print(f"{self.name}'s age is {self.age}")

# print(Person.no_of_person)
# person = Person('Alex', 19)
# person.display()

# person1 = Person.from_birth_year('Adam', 2001)
# person1.display()
# print(Person.no_of_person)

print(date.today().weekday())