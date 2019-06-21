class Fib:
    def __init__(self, k):
        self.fib_numbers = {1 : 1, 2 : 1}
        self.k = k

    def calc(self, n):
        if n in self.fib_numbers:
            return self.fib_numbers[n]
        else:
            self.fib_numbers[n] = self.calc(n - 1) + self.k * self.calc(n - 2)
            return self.fib_numbers[n]


data = open('input.txt').read().strip()
n, k = [int(s) for s in data.split(' ')]
f = Fib(k)
print(f.calc(n))