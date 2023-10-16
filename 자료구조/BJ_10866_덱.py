import sys

input = sys.stdin.readline

n = int(input())
result_list = []

deq_list = [0] * 10000
front_index, rear_index = 0, 0
for i in range(n):
    command = list(map(str, input().split()))

    if command[0] == 'push_front':
        deq_list[front_index] = int(command[1])
        front_index += 1

    if command[0] == 'push_back':
        rear_index -= 1     # 파이썬은 인덱스가 음수가 되면, 리스트의 맨 끝에서부터 시작한다고 보면 된다.
        deq_list[rear_index] = int(command[1])

    if command[0] == 'pop_front':
        # element가 있는 경우 => front_index가 rear_index보다 무조건 크게 된다.
        if front_index-rear_index:
            front_index -= 1
            result_list.append(deq_list[front_index])

        # element가 없는 경우 => front_index와 rear_index가 같다.
        else:
            result_list.append(-1)

    if command[0] == 'pop_back':
        if front_index-rear_index:
            result_list.append(deq_list[rear_index])
            rear_index += 1

        else:
            result_list.append(-1)

    if command[0] == 'size':
        result_list.append(front_index-rear_index)
    if command[0] == 'empty':
        if front_index-rear_index == 0:
            result_list.append(1)
        else:
            result_list.append(0)
    if command[0] == 'front':
        if front_index-rear_index:
            result_list.append(deq_list[front_index-1])
        else:
            result_list.append(-1)
    if command[0] == 'back':
        if front_index-rear_index:
            result_list.append(deq_list[rear_index])
        else:
            result_list.append(-1)

print('\n'.join(map(str, result_list)))