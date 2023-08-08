import sys

input = sys.stdin.readline


def prime_list(_n: int):
    result = []
    sieve = [False, False] + [True] * (2 * _n - 1)
    for i in range(2 * _n + 1):
        if sieve[i]:
            sieve[i] = False
            if i > _n:
                result.append(i)

            for j in range(i + i, 2 * _n + 1, i):
                sieve[j] = False

    return len(result)


input_list = []
while 1:

    n = int(input().strip())
    if n == 0:
        break
    else:
        input_list.append(n)

for number in input_list:
    print(prime_list(number))
