class FibDead:
    def __init__(self, m):
        self.m = m
        self.fibs = {0: 1, 1: 1, 2: 1}

    def fib(self, n):
        if n < 0:
            return 0
        if n in self.fibs:
            return self.fibs[n]
        else:
            self.fibs[n] = self.fib(n - 1) + self.fib(n - 2) - self.fib(n - self.m)
            return self.fibs[n]


with open('input.txt') as f:
    n, m = [int(s) for s in f.read().strip().split(' ')]
    f = FibDead(m + 1)
    print(f.fib(n))