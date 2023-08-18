import sys

input = sys.stdin.readline

prime_list = []

# 방문 처리와 소수 판단이 'check' 리스트 하나로 가능하다.
# 에라토스테네스로 걸러지지 않으면 False가 되는데, 이는 곧 소수를 의미한다.
check = [True, True] + [False] * 999999

# 1 부터 100만 까지의 수를 에라토스테네스의 체를 통해 소수인지 아닌지를 판단하여
# 소수만 모아놓은 prime_list를 미리 만들어 둔다.
for number in range(2, 1000001):
    if check[number]:  # True이면 이미 확인한 수이므로, 볼 필요가 없다.
        continue
    else:
        # 해당 수를 확인해 보지 않았다면,
        # 2는 무조건 소수이므로 일단 append 해도 된다.
        prime_list.append(number)
        for i in range(number+number, 1000001, number):
            check[i] = True

# 1부터 100만까지 엄선된 소수 리스트. 소수의 총 개수는 78498 개이다.
# print(prime_list)
#print(len(prime_list))

# 입력
t = int(input().strip())

result_list = []
for _ in range(t):
    input_number = int(input().strip())

    cnt = 0
    for prime in prime_list:
        # 입력된 수가 엄선된 소수보다 작거나 같다면, 더 이상 볼 필요가 없다.
        # '=' 조건을 통해 자연스럽게 2도 거를 수 있다.
        if prime >= input_number:
            break
        # 입력된 수에서 엄선된 소수를 뺀 수 역시 소수라면, (check[number]=False)
        # 살펴보는 엄선된 소수가 골드바흐 파티션의 파트너 수(?)보다 당연히 작아야 한다. 중복 체크를 피하기 위해서이다.
        if not check[input_number - prime] and prime <= (input_number - prime):
            cnt += 1

    result_list.append(cnt)

# 정답 출력
print("\n".join(map(str, result_list)))
