class DictionaryIter:
    def __init__(self, doct):
        # self.doct = doct
        # self.keys = list(self.doct.keys())
        # self.index = 0
        self.items = list(doct.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items) - 1:
            raise StopIteration

        self.index += 1
        
        return self.items[self.index]


result = DictionaryIter({"name": "Peter", "age": 24})
for x in result:
    print(x)

result = DictionaryIter({1: "1", 2: "2"})
for x in result:
    print(x)
