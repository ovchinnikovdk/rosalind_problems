def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


def permutations(cur, result, seq):
    if len(seq) == 0:
        result.append(cur)
    else:
        for i in range(len(seq)):
            new_cur = cur[:]
            new_cur.append(seq[i])
            permutations(new_cur, result, seq[:i] + seq[i + 1:])

n = 6
print(factorial(n))
result = []
seq = list(range(1, n + 1))
permutations([], result, seq)
for p in result:
    for el in p:
        print(str(el), end=' ')
    print()
