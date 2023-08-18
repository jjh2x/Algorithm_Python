import sys

input = sys.stdin.readline


def findingGCD(a: int, b: int):
    if a < b:
        a, b = b, a

    while b:
        a, b = b, a%b

    # 9자리, 즉 999999999 보다 크다면
    if a >= 1000000000:
        a = str(a)[-9:]     # 맨 끝의 9자리만 출력

    return a


n = int(input().strip())
n_list = list(map(int, input().split()))
n_mul = 1
for i in range(n):
    n_mul *= n_list[i]

m = int(input().strip())
m_list = list(map(int, input().split()))
m_mul = 1
for i in range(m):
    m_mul *= m_list[i]


print(findingGCD(n_mul, m_mul))