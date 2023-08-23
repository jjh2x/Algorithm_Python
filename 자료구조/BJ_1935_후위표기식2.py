import sys

input = sys.stdin.readline

n = int(input().strip())

postfix_str = list(input().strip())
num_list = []

n_ord = []  # 알파벳과 입력 받은 숫자를 매핑시키기 위한 리스트.
for i in range(n):  # n 개의 숫자를 입력 받아서 n_ord 에 저장.
    n_ord.append(int(input().strip()))

for s in postfix_str:
    if s.isalpha():     # s가 알파벳이라면
        # 알파벳을 아스키코드로 바꾼 후, 'A'의 아스키코드인 65를 뺀 값을 인덱스로 사용
        num_list.append(n_ord[ord(s) - 65])

    else:   # s가 연산자라면
        n_2 = num_list.pop()
        n_1 = num_list.pop()
        num_list.append(eval(f"{n_1} {s} {n_2}"))
    # print(f"i: {i} | num_list = {num_list}")

result = num_list.pop()
print("{:.2f}".format(result))

