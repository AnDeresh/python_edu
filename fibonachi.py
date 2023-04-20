# [1, 2, 3, 5, 8...

def recur_fibo(n):
    if n <= 1:
        return n
    return recur_fibo(n - 1) + recur_fibo(n - 2)


def fibo_seq(items):
    return [recur_fibo(i) for i in range(2, items + 2)]


if __name__ == '__main__':
    print(fibo_seq(5))
