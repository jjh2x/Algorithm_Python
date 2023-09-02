import sys
from collections import deque

input = sys.stdin.readline

n = int(int(input().strip()))

queue_list = deque()
result_list = []
for i in range(n):

    command = list(map(str, input().split()))

    # 정수 X를 큐에 넣기
    if command[0] == 'push':
        queue_list.append(int(command[1]))

    # 큐의 가장 첫번째 element 빼기. element 하나도 없으면 -1 출력
    elif command[0] == 'pop':
        if queue_list:
            result_list.append(queue_list.popleft())

        else:
            result_list.append(-1)

    # 큐의 크기 출력
    elif command[0] == 'size':
        result_list.append(len(queue_list))

    # 큐가 비어 있으면 1, 아니면 0 출력
    elif command[0] == 'empty':
        if not queue_list:
            result_list.append(1)
        else:
            result_list.append(0)

    # 큐의 가장 첫번째 element 출력. 큐에 들어 있는 정수 없으면 -1
    elif command[0] == 'front':
        if queue_list:
            result_list.append(queue_list[0])

        else:
            result_list.append(-1)

    # 큐의 가장 마지막 element 출력. 큐에 들어 있는 정수 없으면 -1
    elif command[0] == 'back':
        if queue_list:
            result_list.append(queue_list[-1])

        else:
            result_list.append(-1)

    # print(f"index {i} 명령어 수행 이후 queue_list = {queue_list}")

print('\n'.join(map(str, result_list)))
