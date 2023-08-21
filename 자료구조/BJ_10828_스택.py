import sys

input = sys.stdin.readline

n = int(input().strip())

result_list = []
stack_list = []
for _ in range(n):
    command = list(map(str, input().split()))

    if command[0] == 'push':
        stack_list.append(command[1])

    if command[0] == 'pop':
        if len(stack_list) == 0:
            result_list.append(-1)
        else:
            result_list.append(stack_list.pop())

    if command[0] == 'size':
        result_list.append(len(stack_list))

    if command[0] == 'empty':
        if len(stack_list) == 0:
            result_list.append(1)
        else:
            result_list.append(0)

    if command[0] == 'top':
        if len(stack_list) == 0:
            result_list.append(-1)
        else:
            result_list.append(stack_list[-1])


for r in result_list:
    print(r)