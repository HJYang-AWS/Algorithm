# -*- coding: utf-8 -*-
"""
NxN 배열에 숫자가 들어있다.
한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다.
단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
예를 들어 다음과 같이 배열이 주어진다.

[[2, 1, 2],
 [5, 8, 5],
 [7, 2, 2]]

이 경우 1, 5, 2를 고르면 합이 8로 최소가 된다

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고,
이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.

[입력]
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8

[출력]
#1 8
#2 14
#3 9
"""

T = int(input())
INF = 1e9

def pruning(n, idx, value):
    global min_val
    
    # 가지치기
    if min_val < value:
        return
    
    if idx == n:
        if min_val > value:
            min_val = value
    else:
        for i in range(n): # 행에 대하여 계산
            if not visited[i]:
                visited[i] = 1
                pruning(n, idx + 1, value + matrix[idx][i])
                visited[i] = 0
    
    return min_val
                
                
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    # 방문 노드
    visited = [False for _ in range(n)]
    min_val = INF
    
    print("#{0} {1}".format(test_case, pruning(n, 0, 0)))
    
    
    
    
    
    
    # for i in range(n): # sum_list의 0번부터 n번까지 계산
    #     # check_list 초기화, 선택된 자리가 계산이 됐는지를 true, false로 확인
    #     check_list = [False for _ in range(n)] 
    #     check_list[i] = True
    #     index = 0
    #     min_val = INF
        
    #     for j in range(1, n): # j는 matrix의 2번째 행부터 n번째 행까지
    #         min_val = INF
    #         for idx, val in enumerate(matrix[j]): # k는 check_list에 계산이 안된 자리 확인
    #             if check_list[idx] == False and min_val > val:
    #                 index = idx
    #                 min_val = val
    #         check_list[index] = True
    #         sum_list[i] += min_val
                    
    # print(sum_list)
                
        

    















