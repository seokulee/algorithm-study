strings = open(0).read().splitlines()
N, M = map(int, strings[0].split())

sites = {k: v for k, v in (string.split() for string in strings[1:N+1])}

print(*(sites[string.rstrip()] for string in strings[-M:]), sep='\n')
