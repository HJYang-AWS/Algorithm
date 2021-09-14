import sys
sys.stdin = open("2001. 파리 퇴치_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    fly_map = []
    max_val = 0
    cur_val = 0

    for i in range(N):
        fly_map.append(list(map(int, input().split())))

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            for k in range(M): # window는 MxM
                cur_val += sum(fly_map[i+k][j:j + M])
            if cur_val > max_val:  # 최대값을 찾기
                max_val = cur_val
            cur_val = 0
    print("#{0} {1}".format(test_case, max_val))
