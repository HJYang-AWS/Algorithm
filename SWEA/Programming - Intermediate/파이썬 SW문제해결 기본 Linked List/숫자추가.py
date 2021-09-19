"""
N개의 10억 이하 자연수로 이뤄진 수열이 주어진다.
이 수열은 완성된 것이 아니라 M개의 숫자를 지정된 위치에 추가하면 완성된다고 한다.
완성된 수열에서 인덱스 L의 데이터를 출력하는 프로그램을 작성하시오.
다음은 숫자를 추가하는 예이다.
2 7 -> 2번 인덱스에 7을 추가하고 한 칸 씩 뒤로 이동한다.
4 8 -> 4번 인덱스에 8을 추가하고 한 칸 씩 뒤로 이동한다.

첫줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에
수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L이 주어지고, 다음 줄에 수열이 주어진다.
그 다음 M개의 줄에 걸쳐 추가할 인덱스와 숫자 정보가 주어진다.
5<=N<=1000, 1<=M<=1000, 6<=L<=N+M

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

[입력]
3
5 2 5
1 2 3 4 5
2 7
4 8
5 5 4
13787 32221 32402 32498 4169
3 5902
3 9752
3 27737
1 14133
0 16547
10 10 8
16243 26767 22174 25277 17456 13398 29850 22297 1382 31246
9 23198
7 17514
11 24247
0 25306
2 9104
6 28112
12 7491
10 26972
17 22639
12 28722

[출력]
#1 4
#2 32402
#3 13398
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.count = 0

    # linked_list 끝에 Node를 추가하는 함수
    def add_to_end(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

        # 삽입 함수
    def insert(self, data, index):
        new_node = Node(data)
        idx = 0
        cur = self.head

        if index == 0:
            new_node.next = self.head.next
            self.head.next = new_node
        else:
            # cur은 삽입하려는 부분의 앞 노드
            while idx != index - 1:
                # linked_list의 길이가 입력 index보다 작으면 IndexError
                if cur.next is None:
                    break
                else:
                    cur = cur.next
                    idx += 1

            # new_node 삽입
            new_node.next = cur.next
            cur.next = new_node


# linked_list를 출력하는 함수
    def print(self):
        cur = self.head
        if cur is None:
            print("노드에 데이터가 없습니다.")
        else:
            while True:
                print(cur.data, end=" ")
                if cur.next is None:
                    break
                cur = cur.next

# linked_list의 index번째 data를 출력하는 함수
    def print(self, index):
        cur = self.head
        idx = 0

        if cur is None:
            print("노드에 데이터가 없습니다.")
        else:
            while idx != index:
                if cur.next is None:
                    break
                cur = cur.next
                idx += 1
            return cur.data


T = int(input())

for test_case in range(1, T + 1):
    length, additional_cnt, index_to_print = map(int, input().split())
    # array = [-1, map(int, input().split())]

    sll = SinglyLinkedList()
    for val in input().split():
        sll.add_to_end(val)
    for _ in range(additional_cnt):
        idx, val = map(int, input().split())
        sll.insert(val, idx)
    print("#{0} {1}".format(test_case, sll.print(index_to_print)))

