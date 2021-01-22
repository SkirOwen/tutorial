def fib(n):
    f0, f1 = 0, 1
    while f0 < n:
        print(f0)
        f2 = f1 + f0
        f1, f0 = f2, f1


def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_rec_f(f_max):
    n = 0
    f = fib_rec(n)
    while f < f_max:
        f = fib_rec(n)
        print(f)
        n += 1


if __name__ == "__main__":
    fib(1)