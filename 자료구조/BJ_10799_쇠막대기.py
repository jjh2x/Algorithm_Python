import sys

input = sys.stdin.readline

input_laser_list = list(input().strip())

result_frag_num = 0
temp_stack = []
for i in range(len(input_laser_list)):
    if input_laser_list[i] == '(':
        temp_stack.append('(')
        continue

    elif input_laser_list[i] == ')':
        if input_laser_list[i-1] == '(':    # 현재 괄호가 닫는 괄호이고 바로 전 괄호가 닫는 괄호라면, 이건 레이저다.
            temp_stack.pop()    # 레이저에 해당하는 여는 괄호를 스택에서 빼준다.
            result_frag_num += len(temp_stack)  # 스택에 남아 있는 '(' 개수만큼 조각이 늘아난다.

        else:   # 레이저가 아닌 경우
            temp_stack.pop()
            result_frag_num += 1    # 쇠막대기 하나가 끝남을 의미하므로, 마지막 조각에 해당하는 조각도 카운팅해준다.

print(result_frag_num)



