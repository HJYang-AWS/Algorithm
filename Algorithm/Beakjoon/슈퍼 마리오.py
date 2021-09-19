num_list = []

# input값 받기
for i in range(10):
    num_list.append(int(input()))

# count_list에는 sum값이 들어간다
count_list = [num_list[0]]

for i in range(1, 10):
    count_list.append(count_list[i-1] + num_list[i])
    if count_list[i-1] + num_list[i] > 100:
        break

# 삼항 연산자로 값을 선택
result = count_list[-2] if 100 - count_list[-2] < count_list[-1] - 100 else count_list[-1]

print(result)
