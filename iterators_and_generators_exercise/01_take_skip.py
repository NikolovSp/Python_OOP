class TakeSkip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.count - 1:
            self.index += 1
            return self.index * self.step
        else:
            raise StopIteration


numbers = TakeSkip(2, 6)
for number in numbers:
    print(number)

numbers = TakeSkip(10, 5)
for number in numbers:
    print(number)
