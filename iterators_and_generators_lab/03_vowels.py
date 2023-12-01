class Vowels:
    def __init__(self, txt):
        self.txt = txt
        self.vowels = ["a", "o", "e", "y", "i", "u"]
        self.found = ([char for char in self.txt if char.lower() in self.vowels])
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.found):
            curr_letter = self.found[self.i]
            self.i += 1
            return curr_letter
        else:
            raise StopIteration


my_string = Vowels('Abcedifuty0o')
for char in my_string:
    print(char)
