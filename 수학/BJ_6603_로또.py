import sys

input = sys.stdin.readline


def dfs(current_depth: int, start_index: int):
    if current_depth == 6:
        print(*temp_list)
        return

    for i in range(start_index, list_len):
        temp_list.append(number_list[i])
        #print(f"현재 depth: {current_depth} | iterator : {i}")
        #print(temp_list)

        dfs(current_depth+1, i+1)
        temp_list.pop()


while 1:
    input_list = list(map(int, input().split()))
    list_len = input_list[0]
    number_list = input_list[1:]

    if input_list[0] == 0:
        break

    temp_list = []
    result_list = []
    dfs(0, 0)

    print()
