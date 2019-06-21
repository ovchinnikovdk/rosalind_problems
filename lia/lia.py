K = 2
N = 1

r = N
n = 2 ** K

soch = 1
for i in range(1, r + 1):
    soch *= (n - i + 1)/i
print(soch * 0.25 ** r * 0.75 ** (n - r))