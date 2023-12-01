class SequenceRepeat:
    def __init__(self, txt: str, repeat: int):
        self.txt = txt
        self.repeat = repeat
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.repeat:
            curr_el = self.txt[self.index % len(self.txt)]
            self.index += 1
            return curr_el
        else:
            raise StopIteration


result = SequenceRepeat('abc', 5)
for item in result:
    print(item, end='')

result = SequenceRepeat('I Love Python', 3)
for item in result:
    print(item, end ='')
