def make_trie(anthill, ss):
    for s in ss:
        if s not in anthill:
            anthill[s] = {}

        anthill = anthill[s]


def output(anthill, n):
    for a in sorted(anthill):
        write('--' * n + a + '\n')
        output(anthill[a], n+1)


readline = open(0).readline
write = open(1, 'w').write

N = int(readline())

anthill = {}
for _ in range(N):
    make_trie(anthill, readline().split()[1:])

output(anthill, 0)
