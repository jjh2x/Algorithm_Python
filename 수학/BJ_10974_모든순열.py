import sys

input = sys.stdin.readline

n = int(input().strip())

temp_list = []
visited = [0]*(n+1)


def dfs(current_depth: int):
    if current_depth > n:
        print(*temp_list)
        return

    for i in range(1, n+1):
        if visited[i]:
            continue

        else:
            visited[i] = 1
            temp_list.append(i)

            dfs(current_depth+1)

            temp_list.pop()
            visited[i] = 0


dfs(1)