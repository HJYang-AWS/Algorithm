import sys
sys.stdin = open("1974. 스도쿠 검증_input.txt", "r")


# num_list에 중복이 있으면 True, 아니면 False
def check_overlap(num_list):
    while num_list:
        ele = num_list.pop(0)
        if ele not in num_list:
            continue
        else:
            return True

    return False


def check_sudoku(sudoku_map):
    # 3x3 matrix에 숫자가 안겹치는지 확인
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            num_list = []
            for k in range(3):
                num_list.extend(sudoku_map[i + k][j:j + 3])
            if check_overlap(num_list):
                return 0

    # 세로에 대해 중복이 있는지 확인
    for i in range(9):
        num_list = []
        for j in range(9):
            num_list.append(sudoku_map[j][i])
        if check_overlap(num_list):
            return 0

    # 가로에 대해 중복이 있는지 확인
    for i in range(9):
        if check_overlap(sudoku_map[i]):
            return 0

    # 모두 중복이 없으면
    return 1


T = int(input())

for test_case in range(1, T + 1):
    sudoku = []
    for i in range(9):
        sudoku.append(list(map(int, input().split())))

    print("#{0} {1}".format(test_case, check_sudoku(sudoku)))
