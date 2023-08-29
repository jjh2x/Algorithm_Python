import sys

input = sys.stdin.readline

n = int(input().strip())

number_stack = []
result_opr = []

be_pushed_num = 1
break_bool = False

for i in range(n):
    input_num = int(input().strip())

    # 1부터 입력받은 수까지 모두 스택에 push 되면 while문 탈출
    while be_pushed_num <= input_num:
        number_stack.append(be_pushed_num)
        result_opr.append("+")
        be_pushed_num += 1

    # print(f"({i}+1) 번째 for문 : result_opr = {result_opr}")

    # 현재 스택에서 pop 할 숫자가 입력받은 수라면
    if number_stack[-1] == input_num:
        number_stack.pop()
        result_opr.append("-")
        continue
    # 이미 위에 while문에서 입력받은 수까지 스택에 모두 넣었기 때문에,
    # else 문의 조건은 pop 되어야 하는 수보다 입력받은 수가 더 작은 경우일 것이다.
    # 그렇게 되면, 더 작은 수까지 pop을 계속 해야 하고, 그 다음 턴에 입력 받은 수(현재 턴의 수보다 반드시 클 것)를 절대 꺼낼수가 없게 된다.
    else:
        break_bool = True
        break

if break_bool:
    print("NO")
else:
    print("\n".join(result_opr))

