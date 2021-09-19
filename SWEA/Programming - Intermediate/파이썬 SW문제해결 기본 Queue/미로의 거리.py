"""
NxN 크기의 미로에서 출발지 목적지가 주어진다.
이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를,
경로가 없는 경우 0을 출력한다.
다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐
미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100
0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

[입력]
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
[출력]
#1 5
#2 5
#3 0


"""
import sys
sys.stdin = open('input_미로의 거리.txt', 'r', encoding="UTF-8")


# 이동하려는 위치가 maze_size 보다 작고, 벽이 아닌 경우
def isSafe(ddx, ddy):
    return -1 < ddx < maze_size and -1 < ddy < maze_size and maze[ddx][ddy] != 1


def DFS(maze, n):
    # 위치에 따른 거리를 저장할 2차원 list, distance 변수
    distance = [[0 for _ in range(n)] for _ in range(n)]

    # maze를 방문한 위치를 저장할 visited
    visited = []

    # 시작 위치 찾기, current x, y
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                cx = i
                cy = j
                break

    # 동, 서, 남, 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 갈 수 있는 방향이 2개 이상인 갈림길인 경우, queue에 저장하였다가 돌아감
    q = [[cx, cy]]

    while q:
        cx, cy = q.pop()

        for i in range(4):
            ddx = cx + dx[i]
            ddy = cy + dy[i]
            if isSafe(ddx, ddy) and [ddx, ddy] not in visited:
                if maze[ddx][ddy] == 3:
                    return distance[cx][cy]
                else:
                    distance[ddx][ddy] = distance[cx][cy] + 1
                    visited.append([cx, cy])
                    q.append([ddx, ddy])

    return 0


T = int(input())

for test_case in range(1, T + 1):
    # 미로의 크기
    maze_size = int(input())

    # 0 = 통로, 1 = 벽, 2 = 출발, 3 = 도착
    maze = [[int(i) for i in input()] for _ in range(maze_size)]

    print("#{0} {1}".format(test_case, DFS(maze, maze_size)))






