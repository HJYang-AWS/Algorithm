import sys

sys.stdin = open("input_암호.txt", "r")


class Node:
    def __init__(self, data, prv=None, nxt=None):
        self.data = data
        self.prv = prv
        self.nxt = nxt


class DLL(Node):
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    # self.tail에 값 넣기
    def add_to_tail(self, data):
        new_node = Node(data)
        tail_node = self.tail

        tail_node.nxt = new_node
        new_node.prv = tail_node
        self.tail = new_node

    def print(self):
        cur_node = self.head

        while cur_node.nxt is not None:
            print(cur_node.data, end=" ")
            cur_node = cur_node.nxt
        print(self.tail.data)

    def print_reverse(self):
        cur_node = self.tail

        while cur_node.prv is not None:
            print(cur_node.data, end=" ")
            cur_node = cur_node.prv
        print(self.head.data)

    def print_reverse_10(self):
        cur_node = self.tail

        for _ in range(9):
            if cur_node.prv is not None:
                print(cur_node.data, end=" ")
                cur_node = cur_node.prv
            else:
                print(cur_node.data)
                return
        print(cur_node.data)

    # idx 위치에 값을 삽입하고 it번 반복하는 함수
    def insert(self, idx, it):
        cur_node = self.head

        # it 번 반복
        for _ in range(it):
            # idx번 옮겨가며 cur_node 찾기
            for _ in range(idx):
                if cur_node.nxt is None:
                    cur_node = self.head
                else:
                    cur_node = cur_node.nxt

            # cur_node가 맨 처음일 때, 추가할 값을 맨 앞에 넣기
            if cur_node == self.head:
                new_node = Node(self.head.data + self.tail.data)
                new_node.prv = self.tail
                self.tail.nxt = new_node
                self.tail = new_node
                cur_node = new_node
            else:
                new_node = Node(cur_node.data + cur_node.prv.data)
                new_node.nxt = cur_node
                new_node.prv = cur_node.prv
                cur_node.prv.nxt = new_node
                cur_node.prv = new_node
                cur_node = new_node


T = int(input())

for test_case in range(1, T + 1):
    size, index, iterator = map(int, input().split())
    num_list = list(map(int, input().split()))

    for i in range(size):
        if i == 0:
            node = DLL(num_list[i])
        else:
            node.add_to_tail(num_list[i])

    node.insert(index, iterator)

    print("#{}".format(test_case), end=" ")
    node.print_reverse_10()
