import sys

input = sys.stdin.readline

k = int(input().strip())

num_list = []
for _ in range(k):
    n = int(input().strip())

    if n == 0:
        num_list.pop()

    else:
        num_list.append(n)

print(sum(num_list))