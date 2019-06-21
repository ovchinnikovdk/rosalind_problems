def isPalindrome(s):
    if len(s) % 2 == 1:
        return False
    for i in range(int(len(s)/2)):
        if s[i] == 'C' and s[len(s) - i - 1] != 'G':
            return False
        if s[i] == 'G' and s[len(s) - i - 1] != 'C':
            return False
        if s[i] == 'A' and s[len(s) - i - 1] != 'T':
            return False
        if s[i] == 'T' and s[len(s) - i - 1] != 'A':
            return False
    return True


with open('input.txt') as f:
    dnas = list(filter(lambda x: len(x) > 0, [''.join(x.split()[1:]) for x in f.read().split('>')]))
    palindromes = []
    for dna in dnas:
        for i in range(len(dna)):
            for j in range(4, min(len(dna) - i + 1, 13)):
                if isPalindrome(dna[i:i + j]):
                    palindromes.append([i, j, dna[i:i + j]])
    for start, length, w in palindromes:
        print(str(start + 1) + ' ' + str(length))