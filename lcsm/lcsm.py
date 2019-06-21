from threading import Thread


class FindSubstring(Thread):
    def __init__(self, dnas, substr):
        Thread.__init__(self)
        self.dnas = dnas
        self.substr = substr
        self.success = False

    def run(self):
        for j in range(1, len(dnas)):
            if dnas[j].find(self.substr) == -1:
                self.success = False
                return
        self.success = True


with open('input.txt') as f:
    dnas = list(filter(lambda x: len(x) > 0, [''.join(x.split()[1:]) for x in f.read().split('>')]))
    max_substr = ''
    i = 0
    seq = ''
    num_threads = 8
    step = int(len(dnas) / num_threads)
    while i < len(dnas[0]):
        seq += dnas[0][i]
        threads = []
        for i in range(num_threads):
            thread = FindSubstring(dnas[i * step:(i+1) * step], seq)
            thread.start()
            threads.append(thread)
        for t in threads:
            t.join()
        allSuccess = True
        for t in threads:
            if not t.success:
                allSuccess = False
                break
        if not allSuccess:
            seq = ''
        if len(seq) > len(max_substr):
            max_substr = seq
    print(max_substr)