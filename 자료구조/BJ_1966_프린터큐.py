import sys
from collections import deque

input = sys.stdin.readline

t = int(input().strip())

result_list = []
for _ in range(t):
    n, m = map(int, input().split())
    print_deq = deque(list(map(int, input().split())))

    # 프린터 큐에 걸려 있는 n개의 문서에 대한 순서를 인덱스로 정의
    doc_idx = deque(range(0, n))

    result_count = 0

    while print_deq:
        # 현재 보는 문서의 중요도가 제일 높다면
        if print_deq[0] == max(print_deq):
            # 회전 큐로 무조건 왼쪽으로만 돌리면서 확인할 것이기 때문에, 중요도가 동일한 문서가 나와도
            # 문서가 pop 되어 카운트된다.
            result_count += 1

            # 출력 순서가 궁금했던 문서가 맞다면
            if doc_idx[0] == m:
                break

            # 출력 순서가 궁금했던 문서가 아니라면
            else:
                print_deq.popleft()
                doc_idx.popleft()

        # 현재 보는 문서의 중요도가 제일 높은게 아니라면
        else:
            print_deq.rotate(-1)
            doc_idx.rotate(-1)

            # print(f"doc_idx : {doc_idx}")

    result_list.append(result_count)

print('\n'.join(map(str, result_list)))