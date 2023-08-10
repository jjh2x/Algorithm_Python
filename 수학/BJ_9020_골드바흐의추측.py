import sys

input = sys.stdin.readline


def is_prime(number):
    if number == 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def partioning_number(_number):
    for _ in range(_number//2):
        a, b = _number//2, _number//2

        while a > 0:
            if is_prime(a) and is_prime(b):
                return a, b

            else:
                a -= 1
                b += 1


t = int(input().strip())
number_list = []
for _ in range(t):
    number_list.append(int(input().strip()))

for number in number_list:
    print(' '.join(map(str, partioning_number(number))))