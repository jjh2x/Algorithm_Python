import sys

input = sys.stdin.readline

n = int(input().strip())
num_list = list(map(int, input().split()))
result_list = [-1] * n

temp_stack = []
for i in range(n):
    # 스택에 수가 들어 있고, 현재 살펴보는 수의 크기가 스택의 top의 수의 크기보다 크다면
    while temp_stack and (num_list[i] > temp_stack[-1][0]):
        before_num_info = temp_stack.pop()  # 스택의 top 해당하는 수를 뺀다.
        result_list[before_num_info[1]] = num_list[i]   # 뺀 수의 오큰수가 현재 바라보는 수다.

    # 스택에 수가 없거나(i==0 또는 현재 살펴보는 수가 지금까지 가장 커서 비교대상이 없음)
    # 현재 살펴보는 수의 크기가 스택의 top의 수의 크기보다 작거나 같을 때
    temp_stack.append([num_list[i], i])

print(*result_list)