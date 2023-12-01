class ReverseIter:
    def __init__(self, obj):
        self.obj = obj
        self.i = len(self.obj) - 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.i > -1:
            cur_num = self.obj[self.i]
            self.i -= 1
            return cur_num
        else:
            raise StopIteration()


reversed_list = ReverseIter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
