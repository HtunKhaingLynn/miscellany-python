class Parent():
    def __init__(self, age):
        self._age = age # don't touch from the outside

class Child(Parent):
    def getData(self):
        self._age = 59
        print(self._age)

obj = Child(100)
obj.getData()
print(obj.__dict__)

