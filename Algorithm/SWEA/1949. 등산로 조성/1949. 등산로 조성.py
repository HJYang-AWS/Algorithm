import sys

sys.stdin = open("1949. 등산로 조성_input.txt", "r")


def is_safe(x, y):
    return -1 < x < size and -1 < y < size


def dfs(mountain, x, y):  # mountain:
    # 등산로의 길이를 저장할 변수, matrix
    distance = [[0 for _ in range(size)] for _ in range(size)]
    distance[x][y] = 1
    flat = 1  # 깊이를 한번 팔 경우, flat == 0

    need_visit = [[x, y]]  # stack
    visited = []

    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while need_visit:
        cx, cy = need_visit.pop()  # cx, cy = current_x, current_y

        for _ in range(4):
            if is_safe(cx + dx, cy + dy) and [cx, cy] not in visited:
                # 현재 위치보다 이동한 위치가 더 낮은 경우,
                if table[cx][cy] > table[cx + dx][cy + dy]:
                    cx, cx = cx + dx, cy + dy
                    distance[cx][cy]
                    visited.append([cx][cy])
                    need_visit.append([cx][cy])

                # 현재 위치보다 이동한 위치가 같거나 큰 경우
                else:
                    pass
            else:
                pass

T = int(input())

for test_case in range(1, T + 1):
    size, depth = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(size)]

    # 가장 높은 위치를 저장할 list
    highest_position = []
    max_num = 0
    for i in range(size):
        for j in range(size):
            if table[i][j] > max_num:
                highest_position.clear()
                highest_position.append([i, j])
                max_num = table[i][j]
            elif max_num == table[i][j]:
                highest_position.append([i, j])
            else:
                continue

    for [r, c] in highest_position:
        pass









