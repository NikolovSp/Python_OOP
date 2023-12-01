def genrange(start: int, end: int):
    for i in range(start, end + 1):
        yield start
        start += 1


print(list(genrange(1, 10)))
