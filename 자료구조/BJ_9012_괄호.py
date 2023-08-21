import sys

input = sys.stdin.readline

t = int(input().strip())


def findingVPS(_ps: list):
    if len(_ps) % 2 != 0:
        return 'NO'

    stack_list = []
    for s in _ps:
        if s == '(':
            stack_list.append(s)
        elif s == ')':
            if stack_list:
                stack_list.pop()
                continue
            else:
                return 'NO'

    if stack_list:
        return 'NO'
    else:
        return 'YES'


result_list = []
for _ in range(t):
    ps = list(input().strip())

    result_list.append(findingVPS(ps))

for r in result_list:
    print(r)

