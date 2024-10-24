def make_trie(trie, string):
    for s in string:
        if s not in trie:
            trie[s] = {}

        trie = trie[s]

    trie[None] = None


def check(trie, n):
    count = 0

    def dfs(trie, c):
        nonlocal count

        a = 1 if len(trie) > 1 else 0

        for i in trie:
            if i == None: 
                count += c
                continue

            dfs(trie[i], c+a)

    dfs(trie, 0)
    count += n if len(trie) == 1 else 0

    return count / n


readline = open(0).readline
write = open(1, 'w').write

while True:
    N = readline()
    if N == '': break

    N = int(N)
    trie = {}

    for _ in range(N):
        make_trie(trie, readline().rstrip())

    write(f'{check(trie, N):0.2f}\n')
