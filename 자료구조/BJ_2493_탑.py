import sys
from collections import deque

temp_deq = deque()

input = sys.stdin.readline

n = int(input().strip())

top_height_list = list(map(int, input().split()))

r_top_number = [0]*n  # 모든 탑은 레이저 송신이 안됐다고 가정하고 정답리스트를 0으로 초기화.

for i in range(len(top_height_list)):
    # print(f"현재 i: {i} | 현재 데크 : {temp_deq} | 현재 살펴 보는 탑의 높이 : {top_height_list[i]}")
    while temp_deq:
        # 현재 확인하는 탑의 높이가 이전에 확인한 탑의 높이보다 낮은 경우 (=레이저가 이전 탑들에 의해 송신됨)
        if top_height_list[i] < temp_deq[-1][0]:
            r_top_number[i] = temp_deq[-1][1]   # 이전에 확인한 탑의 위치를 정답 리스트에 넣음

            # print(f"현재 i: {i} | 현재 정답 리스트 : {r_top_number}")
            break   # temp_deq 에 element가 있는지 없는지 기준으로 while문이 도므로, 현재 탑을 확인되었으니, while문을 빠져나가야 함.

        # 현재 확인하는 탑의 높이가 이전에 확인한 탑의 높이보다 높거나 같은 경우 (=새로운 가장 높은 탑이 됨)
        else:
            be_pushed_r = temp_deq.pop()  # 기존의 가장 높은 탑은 이제 확인하지 않아도 됨

    temp_deq.append([top_height_list[i], i+1])    # [높이, 탑 번호]를 데크에 삽입

print(*r_top_number)


