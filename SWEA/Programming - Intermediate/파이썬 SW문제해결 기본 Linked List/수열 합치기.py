import sys

sys.stdin = open('input_수열 합치기.txt', 'r', encoding='UTF-8')


class Node:
    def __init__(self, data, prv=None, nxt=None):
        self.data = data
        self.prv = prv
        self.nxt = nxt


# Doubly Linked List Class
class DLL(Node):
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def add_to_tail(self, data):
        new_node = Node(data)
        tail_node = self.tail

        tail_node.nxt = new_node
        new_node.prv = tail_node
        self.tail = new_node

    def print(self):
        cur_node = self.head

        while cur_node is not None:
            print(cur_node.data, end=" ")
            cur_node = cur_node.nxt

    def print_reverse_10(self):
        cur_node = self.tail

        for i in range(10):
            if i == 9:
                print(cur_node.data)
            else:
                print(cur_node.data, end=" ")
                cur_node = cur_node.prv

    def merge(self, arr):
        cur_node = self.head

        # Node arr이 앞 부분에 위치하는 경우
        if self.head.data > arr.head.data:
            arr.tail.nxt = self.head
            self.head.prv = arr.tail
            self.head = arr.head
        else:
            while cur_node.nxt is not None:
                if cur_node.data <= arr.head.data < cur_node.nxt.data:
                    arr.head.prv = cur_node
                    arr.tail.nxt = cur_node.nxt
                    cur_node.nxt = arr.head
                    arr.tail.nxt.prv = arr.tail
                    break
                else:
                    cur_node = cur_node.nxt

            if cur_node.nxt is None:
                self.tail.nxt = arr.head
                arr.head.prv = self.tail
                self.tail = arr.tail


T = int(input())

for test_case in range(1, T + 1):
    length, num = map(int, input().split())
    num_list = [list(map(int, input().split())) for _ in range(num)]
    node_list = [0] * num

    for i in range(num):
        node_list[i] = DLL(num_list[i][0])
        for j in range(1, length):
            node_list[i].add_to_tail(num_list[i][j])

        if i != 0:
            node_list[0].merge(node_list[i])

    print("#{}".format(test_case), end=" ")
    node_list[0].print_reverse_10()


