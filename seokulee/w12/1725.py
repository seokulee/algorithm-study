def solution(heights):
    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = heights[top_of_stack] * (index if not stack else index - stack[-1] - 1)
            max_area = max(max_area, area)

    while stack:
        top_of_stack = stack.pop()
        area = heights[top_of_stack] * (index if not stack else index - stack[-1] - 1)
        max_area = max(max_area, area)

    return max_area


import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:N+1]))

# Output the solution
print(solution(A))
