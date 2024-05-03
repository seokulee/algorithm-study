import sys

chat_list = set()
count = 0

N = int(sys.stdin.readline())

for _ in range(N):
    input = sys.stdin.readline().rstrip()
    if input == "ENTER":
        count += len(chat_list)
        chat_list.clear()
    else:
        chat_list.add(input)

count += len(chat_list)
print(count)
