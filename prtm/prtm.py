def load_mass_table():
    with open('mass_table.txt') as f:
        masses = f.read().split('\n')
        print(masses)
        table = dict()
        for mass in masses:
            key, value = mass.split()
            table[key] = float(value)
        return table


with open('input.txt') as f:
    protein = f.read().strip()
    table = load_mass_table()
    print(sum(table[p] for p in protein))