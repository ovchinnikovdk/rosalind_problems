
dna = open('input.txt', 'r').read().strip()

counters = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}

for ch in dna:
    counters[ch] += 1

for key in counters.keys():
    print(str(counters[key]) + " ")