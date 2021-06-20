class Parent:
    pass

class Child(Parent):
    pass

print(issubclass(Child, Parent)) # check first one is sub class of sec one

obj = Child()
print(isinstance(obj, Child)) # check first one is instance of sec Class
print(isinstance(obj, Parent))