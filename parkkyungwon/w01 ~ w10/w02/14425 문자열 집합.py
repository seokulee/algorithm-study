import sys



readline = sys.stdin.readline
m_count, c_count = map(int, readline().split())

m_set = {readline() for _ in range(m_count)}

included_count = 0
for _ in range(c_count):
    if readline() in m_set: included_count += 1

print(included_count)
