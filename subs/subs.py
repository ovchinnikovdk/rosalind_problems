with open('input.txt') as f:
    s, t = f.read().split()
    subs = []
    lent = len(t)
    for i in range(len(s) - lent):
        if s[i: i + lent] == t:
            subs.append(i + 1)
    res = ''
    for i in subs:
       res += str(i) + ' '
    print(res)