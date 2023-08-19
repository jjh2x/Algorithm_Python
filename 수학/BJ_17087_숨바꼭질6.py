import sys

input = sys.stdin.readline

# 입력 부분
n, s = map(int, input().split())
a_list = list(map(int, input().split()))

# 수빈이와 동생들이 한 선 상에 모두 같이 있다고 생각하여 한 리스트에 모두 넣는다.
a_list = [s] + a_list
a_list.sort()

a_list_diff = []
# 각 element 들의 차를 구한 값들을 a_list_diff 에 넣는다.
for i in range(len(a_list)-1, 0, -1):
    temp_diff = a_list[i] - a_list[i-1]
    a_list_diff.append(temp_diff)


# 최대 공약수 구하는 함수
def findingGCD(a: int, b: int):
    if a < b:
        a, b = b, a

    while b:
        a, b = b, a%b

    return a


def solve(diff_list: list):
    currentGCD = max(a_list_diff)
    # 각 element들의 차에 대한 최대 공약수를 구한다.
    for i in range(len(diff_list)):
        currentGCD = findingGCD(currentGCD, diff_list[i])

    return currentGCD


result_number = solve(a_list_diff)
print(result_number)
