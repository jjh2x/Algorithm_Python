import sys

input = sys.stdin.readline

n, s = map(int, input().split())

number_list = list(map(int, input().split()))

result_count = 0
answer_list = []
def dfs(start_index:int):
    global result_count
    if start_index >= n:
        return

    answer_list.append(number_list[start_index])
    if sum(answer_list) == s:
        result_count += 1

    # print(f"answer_list = {answer_list}")

    dfs(start_index+1)

    answer_list.pop()
    dfs(start_index+1)


dfs(0)
print(result_count)

