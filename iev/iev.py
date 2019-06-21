with open('input.txt') as f:
    genotypes = [float(s) for s in f.read().strip().split(' ')]
    pr = [1., 1., 1., 3./4., 1./2., 0.]
    print(sum([2. * g * p for g, p in zip(genotypes, pr)]))