import sys

input = sys.stdin.readline
n, m = map(int, input().split())
number_list = []

visited = [True] + [False] * n


def dfs():
    # m 개의 숫자가 리스트에 모였다면,
    if len(number_list) == m:
        print(' '.join(map(str, number_list)))
        return  # dfs() 함수를 종료
    for i in range(1, n + 1):
        if visited[i]:  # 해당 숫자를 이미 사용했다면,
            continue  # for문을 다음으로 넘긴다.

        # i 라는 숫자로 시작을 하는 수열은
        visited[i] = True  # i 라는 숫자 사용하였으니, 방문 처리
        number_list.append(i)  # i 라는 숫자로 시작을 하는 수열 만들기 위해 리스트에 element 추가
        # print(visited)    # number_list에 숫자가 추가된 상태, 방문 정보를 가지고 dfs 를 다시 수행
        dfs()  # i 라는 숫자로 시작을 하는 수열에 대해 나머지 부분에 대한 수열도 생성

        # 가장 마지막의 dfs() 함수에서 수열이 도출 되므로,
        # 이번 iterator 에서 사용한 숫자는 초기화.
        # (=다음 iterator, 즉, 첫번째로 시작하는 숫자를 따질 때에는 이번 iterator의 숫자는 사용되지 않은 상태여야 함.)
        number_list.pop()
        # print(number_list)

        visited[i] = False  # pop()과 같은 맥락.


dfs()