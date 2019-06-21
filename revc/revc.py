dna = open('input.txt').read().strip()
result = [None] * len(dna)
complement = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
for i in range(len(dna)):
    result[len(result) - i - 1] = complement[dna[i]]

print(''.join(result))