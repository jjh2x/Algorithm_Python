import sys

input = sys.stdin.readline

n = 1000001
prime_list = [0] + [1] * n

# 2는 소수지만, 이 문제에서는 짝수 소수는 조건을 만족하지 않으므로 제외 '소수 리스트'에서도 제외
for i in range(3, int(n**0.5)+1, 2):
    if prime_list[i]:
        for j in range(2*i, n, i):  # 짝수 및 소수가 아닌 홀수들은 모두 0으로 만들기
            prime_list[j] = 0

result_list = []
while 1:
    breaker=False

    t = int(input().strip())
    if t == 0:
        break

    for i in range(3, (t//2)+1, 2):
        if prime_list[i] and prime_list[t-i]:
            print(f"{t} = {i} + {t-i}")
            breaker = True
            break

    if breaker:
        continue
    else:
        result_list.append("Goldbach's conjecture is wrong.")

for r_str in result_list:
    print(r_str)
