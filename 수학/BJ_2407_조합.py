import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def factorial(number: int):
    a = 1
    if number == 0 or number == 1:
        return a

    for i in range(2, number+1):
        a *= i

    return a


result = factorial(n) // (factorial(n-m)*factorial(m))

print(result)