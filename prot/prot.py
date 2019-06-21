def load_table():
    with open('codon_table.txt') as f:
        table = dict()
        s = f.read().split('\n')
        for row in s:
            key, value = row.split(' ')
            table[key] = value
        return table

with open('input.txt') as f:
    rna = f.read().strip()
    protein = ''
    table = load_table()
    for i in range(0, len(rna), 3):
        if table[rna[i: i + 3]] == 'Stop':
            break
        protein += table[rna[i: i + 3]]
    print(protein)