import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
be_popped_number = list(map(int, input().split()))

deq = deque(range(1, n+1))

result_count = 0
for compared_number in be_popped_number:
    while deq:
        if compared_number == deq[0]:
            deq.popleft()
            break

        else:
            # 데크를 반으로 쪼개었을 때,
            # 찾으려는 원소의 인덱스가 반보다 작거나 같은 경우 => 왼쪽으로 가는게 이득
            if deq.index(compared_number) <= (len(deq) // 2):
                deq.rotate(-1)
                result_count += 1
            else:
                deq.rotate(1)
                result_count += 1

print(result_count)
