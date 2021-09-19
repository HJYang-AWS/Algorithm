# -*- coding: utf-8 -*-
"""
사다리 게임이 지겨워진 알고리즘 반 학생들이 새로운 게임을 만들었다.
가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑는 것이다.

게임 룰은 다음과 같다.
1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다. 전체를 두 개의 그룹으로 나누고,
그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.
그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데,
i번부터 j번까지 속한 그룹은 파이썬 연산으로 두개로 나눈다.

두 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가리고,
다시 더 큰 그룹의 승자를 뽑는 방식이다.
다음은 4명이 카드를 비교하는 경우로, 
숫자 1은 가위, 2는 바위, 3은 보를 나타낸다. 
만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자로 하고, 
처음 선택한 카드는 바꾸지 않는다.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 별로 인원수 N과 다음 줄에 N명이 고른 카드가 번호순으로 주어진다.
4≤N≤100
카드의 숫자는 각각 1은 가위, 2는 바위, 3은 보를 나타낸다. 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 1등의 번호를 출력한다.

[입력]
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3

[출력]
#1 3
#2 5
#3 1
"""

T = int(input())


# 1 = '가위', 2 = '바위', 3 = '보'
def rsp(a, b):
    if (a[1] - b[1] == -1) or (a[1] == 3 and b[1] == 1):
        return b
    else:
        return a



def card_game(c_list):
    global winner_list

    if len(c_list) == 1:
        return winner_list.append(c_list[0])
    elif len(c_list) == 2:
        return winner_list.append(rsp(c_list[0], c_list[1]))
    else:
        start = 0
        end = len(c_list) - 1
        middle = (start + end) // 2 + 1
        front = c_list[:middle]
        back = c_list[middle:]
        card_game(front)
        card_game(back)


for test_case in range(1, T + 1):
    num = int(input())
    # card_list = [플레이어번호, 값]
    card_list = [[i + 1, val] for i, val in enumerate(list(map(int, input().split())))]

    while len(card_list) != 1:
        winner_list = []
        card_game(card_list)
        card_list = winner_list
    
    print("#{0} {1}".format(test_case, card_list[0][0]))
