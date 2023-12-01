def reverse_text(txt):
    start = len(txt) - 1
    end = 0
    while start >= end:
        yield txt[start]
        start -= 1


for char in reverse_text("step"):
    print(char, end='')
