import sys
sys.stdin = open("3499. 퍼펙트 셔플_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    size = int(input())
    str_list = list(map(str, input().split()))
    shuffle_A = []
    shuffle_B = []
    result = []

    for idx in range(size):
        # 두 개로 나눠주고 전체가 홀수 일 때, shuffle_A가 하나 더 많음
        if idx < (size + 1) // 2:
            shuffle_A.append(str_list[idx])
        else:
            shuffle_B.append(str_list[idx])

    print(shuffle_A)
    print(shuffle_B)

    for idx in range(size):
        if idx % 2 == 0:
            result.append(shuffle_A.pop(0))
        else:
            result.append(shuffle_B.pop(0))

    print("#{0} {1}".format(test_case, " ".join(result)))
