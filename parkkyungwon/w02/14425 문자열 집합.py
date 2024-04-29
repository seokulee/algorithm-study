m_count, c_count = map(int, input().split())

m_set = {input() for _ in range(m_count)}

included_count = 0
for _ in range(c_count):
    if input() in m_set:
        included_count += 1

print(included_count)
