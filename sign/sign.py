def perm(cur, result, base):
    if len(base) == 0:
        result.append(cur)
    else:
        for el in base:
            new_cur = cur[:]
            new_cur.append(el)
            new_base = base[:]
            new_base.remove(el)
            if -el in new_base:
                new_base.remove(-el)
            perm(new_cur, result, new_base)


with open('input.txt') as f:
    n = int(f.read().strip())
    base = []
    for i in range(1, n + 1):
        base.append(i)
        base.append(-i)
    result = []
    cur = []
    perm(cur, result, base)
    print(len(result))
    for permut in result:
        for el in permut:
            print(el, end=' ')
        print()