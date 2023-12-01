class CountdownIterator:
    def __init__(self, count: int):
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.index:
            num = self.count
            self.count -= 1
            return num
        else:
            raise StopIteration


iterator = CountdownIterator(10)
for item in iterator:
    print(item, end=" ")

iterator = CountdownIterator(0)
for item in iterator:
    print(item, end=" ")
