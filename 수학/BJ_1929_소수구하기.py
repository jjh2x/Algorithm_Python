import sys

input = sys.stdin.readline

m, n = map(int, input().split())


def prime_list(_m, _n):
    sieve = [False, False] + [True]*(_n - 1)

    # n의 약수 중 최대 소수는 sqrt(n) 이하이므로, i=sqrt(n) 까지 검사
    k = int(_n ** 0.5)
    for i in range(2, k+1):
        if sieve[i]:
            for j in range(i+i, _n+1, i): # i 이후 i의 배수들을 False 판정
                sieve[j] = False

    for r in range(_m, _n):
        if sieve[r]:
            print(r)


prime_list(m, n)