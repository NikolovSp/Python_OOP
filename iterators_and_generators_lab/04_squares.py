def squares(n):
    # for i in range(1, n + 1):
    #     yield i ** 2
    #     i += 1
    i = 1
    while i <= n:
        yield i ** 2
        i += 1


print(list(squares(5)))
