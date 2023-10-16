import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())
heap = []

for _ in range(n):
    x = int(input().strip())

    if x != 0:
        # 절댓값을 기준으로 힙에 넣고,
        # 출력할 때에는 원래 값을 가져와야 하므로, 다음과 같이 튜플 형태로 힙에 넣는다.
        heapq.heappush(heap, (abs(x), x))

    else:
        if len(heap):
            print(heapq.heappop(heap)[1])

        else:
            print(0)

