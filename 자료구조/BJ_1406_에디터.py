import sys

input = sys.stdin.readline

init_str = list(input().strip())
forStack_list = []

n = len(init_str)
m = int(input().strip())

for _ in range(m):

    command_str = list(map(str, input().split()))
    # print(f"명령어 수행 전 :  init_str = {init_str}, forStack_list = {forStack_list}")

    # 커서 왼쪽으로 한 칸 옮김
    if command_str[0] == 'L':
        if init_str:
            forStack_list.append(init_str.pop())
        else:   # 커서가 가장 왼쪽에 있는 경우는 init_str 리스트의 element가 없는 경우임.
            continue

    # 커서를 오른쪽으로 한 칸 옮김
    if command_str[0] == 'D':
        if forStack_list:
            init_str.append(forStack_list.pop())
        else:   # 커서가 가장 오른쪽에 있는 경우는 forStack_list 리스트의 element가 없는 경우임.
            continue

    # 커서 왼쪽에 있는 문자를 삭제
    if command_str[0] == 'B':
        if init_str:
            init_str.pop()

    # 인자로 받은 값을 커서 왼쪽에 추가
    if command_str[0] == 'P':
        init_str.append(command_str[1])

    # print(f"명령어 수행 후 :  init_str = {init_str}, forStack_list = {forStack_list}")

init_str.extend(reversed(forStack_list))
print(''.join(init_str))

