txt = input()

txt_len = len(txt)
total_com = 0
for n in range(1, txt_len + 1):

    tem_set = set()
    for i in range(txt_len - n + 1):
        tem_set.add(txt[i : i+n])

    total_com += len(tem_set)

print(total_com)
