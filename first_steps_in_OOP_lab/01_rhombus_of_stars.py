def print_shape(n_, i_):
    print(" " * (n_ - i_), end="")
    print(*["*"] * i_)


n = int(input())

for i in range(1, n + 1):
    print_shape(n, i)

for i in range(n - 1, 0, -1):
    print_shape(n, i)
