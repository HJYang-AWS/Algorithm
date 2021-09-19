"""
V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.
{1: [4, 3],
 2: [3, 5],
 3: [1, 2],
 4: [1, 6]
 5: [2],
 6:[4]}

노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.
E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
두 노드 S와 G가 서로 연결되어 있지 않다면, 0을 출력한다.

[입력]
3       T
6 5     V, E
1 4     E=1
1 3     E=2
2 3     E=3
2 5     E=4
4 6     E=5
1 6     S, G
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

#1 2
#2 4
#3 3
"""
import sys

sys.stdin = open("input_노드의거리.txt", "r", encoding="UTF-8")


T = int(input())


def find_node(start, end):  # DFS
    # need_visit == 방문할 노드
    need_visit = [start]

    cost = 0  # cost == 이동거리
    node_cost = {start: cost}  # node로 이동할 때, cost 저장

    while need_visit:  # DFS
        cur_node = need_visit.pop()  # cur_node = 현재 노드
        cost = node_cost[cur_node]  # cost는 현재 노드로 이동할 때 드는 비용

        next_node = graph[cur_node]  # 다음 노드의 정보를 next_node에 저장
        for nxt in next_node:  # next_node의 원소 nxt
            if nxt not in node_cost.keys():  # nxt가 visited에 없다면
                need_visit.extend([nxt])
                node_cost.update({nxt: cost+1})
            else:  # nxt가 visited에 있지만 cost값이 더 작을 때
                if node_cost[nxt] > cost+1:
                    need_visit.extend([nxt])
                    node_cost.update({nxt: cost + 1})

    if end in node_cost.keys():
        return node_cost[end]
    else:
        return 0


for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    graph = {}

    # node 만들기
    for i in range(e):
        node, linked_node = map(int, input().split())

        # node에 대한 linked_node 정보 graph에 추가
        if node not in graph.keys():  # node에 정보가 없을 때
            graph.update({node: [linked_node]})
        else:
            graph[node].append(linked_node)

        # 방향이 없으므로 linked_node에 대한 node 정보 graph에 추가
        if linked_node not in graph.keys():  # linked_node에 정보가 없을 때
            graph.update({linked_node: [node]})
        else:
            graph[linked_node].append(node)

    s, g = map(int, input().split())

    print("#{0} {1}".format(test_case, find_node(s, g)))

