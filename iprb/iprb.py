with open('input.txt') as f:
    k, m, n = [float(s) for s in f.read().strip().split(' ')]
    N = k + n + m
    print((k * (k - 1) + 3./4. * m * (m - 1) + 2 * m * k + 2. * n * k + m * n) / (N * (N - 1)))