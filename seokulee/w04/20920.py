import sys

N, M = map(int, sys.stdin.readline().split())
note = dict()

for _ in range(N):
    input = sys.stdin.readline().rstrip()

    if len(input) >= M:
        if input in note.keys():
            note[input] += 1
        else:
            note[input] = 1

final_note = sorted(note.keys(), key=lambda x : (-note[x], -len(x), x))

print('\n'.join(final_note))
