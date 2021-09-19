# -*- coding: utf-8 -*-
"""
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오.
도착할 수 있으면 1, 아니면 0을 출력한다. 주어진 미로 밖으로는 나갈 수 없다.
 
다음은 5x5 미로의 예이다.
13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.  

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다.
0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

"""


def isSafe(ddx, ddy):
    return -1 < ddx < maze_size and -1 < ddy < maze_size and maze[ddx][ddy] != 1


def bfs(maze):
    # 시작 위치 찾기
    for i in range(maze_size):
        for j in range(maze_size):
            if maze[i][j] == 2:
                xs, ys = i, j
    
    # 12시, 3시, 6시, 9시
    dx = [-1, 0, 1 ,0]
    dy = [0, 1, 0, -1]
    
    # 방문한 미로 설정, 0: 미방문, 1: 방문
    visited = [[0 for _ in range(maze_size)] for _ in range(maze_size)]
    visited[xs][ys] = 1
    
    queue = [[xs, ys]]
    
    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            
            if isSafe(ddx, ddy) and visited[ddx][ddy] == 0:
                visited[ddx][ddy] = 1
                queue.append([ddx, ddy])
                if isSafe(ddx, ddy) and maze[ddx][ddy] == 3:
                    return 1
    
    return 0


T = int(input())

for test_case in range(1, T + 1):
    global maze_size
    maze_size = int(input())
    global maze
    maze = [list(map(int, input())) for _ in range(maze_size)]

    print("#{0} {1}".format(test_case, bfs(maze)))

    
















