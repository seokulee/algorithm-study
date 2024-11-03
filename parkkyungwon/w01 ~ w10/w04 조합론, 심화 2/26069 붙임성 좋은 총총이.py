import sys



readline = sys.stdin.readline

N = int(readline().strip())
dance = {"ChongChong"}

for _ in range(N):
    people = readline().strip().split()

    if people[0] in dance or people[1] in dance:
        dance.update(people)

print(len(dance))
