txt = input()

for i in range(len(txt) // 2):
    if txt[i] != txt[-(i + 1)]:
        print(0)
        break
else:
    print(1)
