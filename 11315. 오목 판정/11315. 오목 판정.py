import sys
sys.stdin = open("11315. 오목 판정_input.txt", 'r')

T = int(input())


def is_safe(ddr, ddc):
    size = len(matrix)
    return -1 < ddr < size and -1 < ddc < size and matrix[ddr][ddc] == 'o'


def omok(baduk_board):
    length = len(baduk_board)

    # 오른쪽, 아래, 왼쪽아래 대각선, 오른쪽아래 대각선
    dr = [0, 1, 1, 1]
    dc = [1, 0, -1, 1]

    for r in range(length):
        for c in range(length):
            if baduk_board[r][c] == 'o':
                cnt = 1

                # 오른쪽, 아래, 왼쪽아래, 오른쪽아래
                for i in range(4):
                    ddr = r
                    ddc = c
                    for _ in range(4):
                        # 가로에 대해 오목을 확인
                        ddr += dr[i]
                        ddc += dc[i]
                        if is_safe(ddr, ddc):
                            cnt += 1
                            if cnt == 5:
                                return "YES"
                        else:
                            ddr = r
                            ddc = c
                            cnt = 1
                            break

    return "NO"


for test_case in range(1, T + 1):
    N = int(input())
    matrix = []

    for i in range(N):
        matrix.append(list(input()))

    # print(matrix)
    print("#{0} {1}".format(test_case, omok(matrix)))
