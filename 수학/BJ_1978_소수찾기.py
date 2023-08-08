import sys

input = sys.stdin.readline

n = int(input().strip())

n_list = list(map(int, input().split()))

result = 0
for number in n_list:
    if number == 1:
        continue

    this_number = True
    for i in range(2, number):
        if number % i != 0:
            continue
        else:
            this_number = False
            break

    if this_number:
        result += 1


print(result)