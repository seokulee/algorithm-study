def make_trie(trie, string):
    for s in string:
        if s not in trie:
            trie[s] = {}

        trie = trie[s]

    trie[None] = None


def check(trie, string):
    for s in string:
        if s not in trie: return False
        
        trie = trie[s]
    
    return True if None in trie else False


readline = open(0).readline
write = open(1, 'w').write

N, M = map(int, readline().split())

trie = {}
count = 0

for _ in range(N):
    make_trie(trie, readline().rstrip())

for _ in range(M):
    count += check(trie, readline().rstrip())

print(count)
