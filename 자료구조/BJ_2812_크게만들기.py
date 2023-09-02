import sys

input = sys.stdin.readline

n, k = map(int, input().split())
num_list = list(map(int, input().strip()))

# result_list = [0] * n

temp_stack = []
for i in range(n):
    while temp_stack and k > 0 and temp_stack[-1] < num_list[i]:
        temp_stack.pop()
        k -= 1

    temp_stack.append(num_list[i])

# 만약 주어진 숫자를 다 체크했는데, k가 아직 0보다 크다면(빼야 하는 수가 더 남았다면)
# temp_stack 의 맨 끝에서부터 k개만큼을 빼주고 나머지를 출력해야 한다.
print(''.join(map(str, temp_stack[:len(temp_stack)-k])))

