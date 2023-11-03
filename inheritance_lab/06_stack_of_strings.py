class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


my = Stack()
print(my.is_empty())
my.push('a')
my.push('c')
print(my.__str__())
print(my.is_empty())

