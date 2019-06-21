def gc_content(dna):
    count = 0
    for ch in dna:
        if ch == 'G' or ch == 'C':
            count += 1
    return count / len(dna) * 100.


def prepare(line):
    lst = line.split()
    if len(lst) < 2:
        return None
    return lst[0], ''.join(lst[1:])


with open('input.txt') as f:
    dnas = list(filter(lambda x: x is not None and len(x[1]) > 0, [prepare(x) for x in f.read().split('>')]))
    max_content = gc_content(dnas[0][1])
    max_id = dnas[0][0]
    for id, dna in dnas:
        content = gc_content(dna)
        if content > max_content:
            max_id = id
            max_content = content
    print(max_id)
    print(max_content)