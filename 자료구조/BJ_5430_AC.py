import sys
from collections import deque

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    p_list = list(input().strip())  # 'R'과 'D'로 이루어진 명령 리스트
    n = int(input().strip())
    num_list = input().strip()[1:-1].split(",")
    # print(f"t: {t} | num_list: {num_list}")
    deq = deque(num_list)

    flag = 0
    break_check = False
    for p in p_list:
        if p == 'R':
            # 최종 결과에서 딱 한 번만 뒤집을 지 말지 flag에 따라 결정한다.
            flag += 1
            continue

        elif p == 'D':
            if len(deq) == 0 or deq[0] == '':
                print("error")
                break_check = True
                break

            else:
                # R의 횟수가 짝수이면, 뒤집지 않아도 된다.
                # => 가장 앞의 수를 버린다.
                if flag % 2 == 0:
                    deq.popleft()

                # R의 횟수가 홀수이면, 뒤집어야 한다.
                # 뒤집은 걸 가정하므로, 가장 뒤의 수부터 버려야 한다.
                else:
                    deq.pop()

    if break_check:
        # break문을 통해 더 이상의 원소가 없다면, 다음 테스트 케이스로 넘어간다.
        continue

    if flag % 2 == 0:
        print("[" + ",".join(deq) + "]")

    else:
        deq.reverse()
        print("[" + ",".join(deq) + "]")

