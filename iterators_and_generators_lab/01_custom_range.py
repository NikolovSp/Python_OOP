class CustomRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            cur_num = self.start
            self.start += 1
            return cur_num
        else:
            raise StopIteration()


one_to_ten = CustomRange(1, 10)
for num in one_to_ten:
    print(num)
