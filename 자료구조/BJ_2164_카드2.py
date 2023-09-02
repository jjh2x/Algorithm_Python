import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())

card_list = deque()
for number in range(1, n+1):
    card_list.append(number)


def card_making(_card_list: deque):
    while len(_card_list) != 1:
        # 제일 위에 있는 카드를 버린다.
        _card_list.popleft()

        # 그 다음 제일 위에 있는 카드를 가장 아래로 옮긴다.
        _card_list.append(_card_list.popleft())

    print(_card_list[-1])


card_making(card_list)