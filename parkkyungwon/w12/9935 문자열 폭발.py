def find(ori_str, pattern):
    L = len(pattern)
    pattern = list(pattern)
    stack = []

    for s in ori_str:
        stack.append(s)

        # 패턴의 뒤에서 앞으로 확인
        if len(stack) >= L and stack[-1] == pattern[-1] and stack[-L:] == pattern:
            del stack[-L:]

    return ''.join(stack) if stack else 'FRULA'


ori_str = input()
pattern = input()

print(find(ori_str, pattern))
