class Stack:
    def __init__(self) -> None:
        self.item = []

    def push(self, *data):
        for d in data:
            self.item.append(d)

    def pop(self):
        return self.item.pop()

    def peek(self):
        print(f'{self.item[len(self.item) - 1]} was peeked')
        self.pop()

    def is_empty(self):
        return True if len(self.item) == 0 else False

    def show_stack(self):
        if len(self.item) != 0:
            return self.item
        else:
            return 'Your stack is empty.'

stack = Stack()
stack.push(1,2,3,4,'koko')
stack.peek()
stack.pop()
print(stack.show_stack())
print(stack.is_empty())