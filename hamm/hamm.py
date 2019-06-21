def ham_dist(s, t):
    return len(list(filter(lambda x: x[0] != x[1], zip(s, t))))


with open('input.txt') as f:
    s, t = f.read().split()
    print(ham_dist(s, t))
