class Parent():
    def __init__(self, age):
        self.__age = age

class Child(Parent):
    def update(self, new_age):
        self.__age = new_age
        return self.__age

    def show(self):
        self.__age = 59
        print(self.__age)

obj = Child(100)
print(obj.update(50))
obj.show()
print(obj.__dict__)
