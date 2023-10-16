import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

current_people = deque([p for p in range(1, n+1)])

result_list = []

for i in range(n):

    # 한 사람을 제거하는 루틴에서 그 사람이 제거할 대상이 맞는 지 체크할 변수 저장
    # k 보다 적은 사람이 남은 경우에는, '코카콜라 맛있다' 처럼 번갈아 가기 때문에,
    # 현재 내가 몇 번을 세었는지 저장할 current_count 를 선언
    current_count = 1

    # 제거는 회전 큐의 가장 첫번째 원소에서 진행된다.
    # K번째 사람이 아닌 경우, 회전 큐를 왼쪽으로 돌린다.
    while current_count != k:
        # print(f"현재 i : {i} | current_idx : {current_idx} | current_people : {current_people}")
        current_people.rotate(-1)
        current_count += 1

    result_list.append(current_people.popleft())

print("<" + ', '.join(map(str, result_list)) + ">")
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

current_people = deque([p for p in range(1, n+1)])

result_list = []

for i in range(n):

    # 한 사람을 제거하는 루틴에서 그 사람이 제거할 대상이 맞는 지 체크할 변수 저장
    # k 보다 적은 사람이 남은 경우에는, '코카콜라 맛있다' 처럼 번갈아 가기 때문에,
    # 현재 내가 몇 번을 세었는지 저장할 current_count 를 선언
    current_count = 1

    # 제거는 회전 큐의 가장 첫번째 원소에서 진행된다.
    # K번째 사람이 아닌 경우, 회전 큐를 왼쪽으로 돌린다.
    while current_count != k:
        # print(f"현재 i : {i} | current_idx : {current_idx} | current_people : {current_people}")
        current_people.rotate(-1)
        current_count += 1

    result_list.append(current_people.popleft())

print("<" + ', '.join(map(str, result_list)) + ">")
