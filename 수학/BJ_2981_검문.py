import sys

input = sys.stdin.readline

n = int(input().strip())
number_list = [int(input()) for _ in range(n)]
number_list.sort()

diff_list = []
for i in range(len(number_list)-1, 0, -1):
    diff_list.append(number_list[i] - number_list[i-1])


# 두 수 a,b의 최대 공약수를 구하는 함수
def findingGCD(a: int, b: int):
    if a < b:
        a, b = b, a

    while b:   # y가 0이 아니라면
        a, b = b, a%b
    return a

# 각 수들의 차가 담긴 list에서 수 하나씩 비교하여 모든 수들의 최대 공약수를 구한다.
n_gcd = diff_list[0]
for j in range(1, len(diff_list)):
    n_gcd = findingGCD(n_gcd, diff_list[j])

result_list = []    # 정답이 담길 리스트
# 모든 수들의 최대공약수의 약수들을 구하는데,
# 이때, 해당 최대공약수의 제곱근까지만 따져보면, 약수를 구하는 최소 반으로 줄일 수 있다.
for k in range(2, int(n_gcd**0.5)+1):
    if n_gcd % k == 0:
        result_list.append(k)
        result_list.append(n_gcd//k)

# 위 과정에서는 최대공약수의 제곱근까지만 살펴보았으므로, 최대공약수 자신도 result_list에 넣어주어야 한다.
result_list.append(n_gcd)

# result_list의 각 element들의 중복 제거
result_list = list(set(result_list))

# result_list를 오름차순으로 정렬
result_list.sort()

print(*result_list)