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

        # new_node = Node(data)
        # cur_node = self.head
        #
        # while cur_node.nxt is not None:
        #     cur_node = cur_node.nxt
        #
        # cur_node.nxt = new_node
        # new_node.prv = cur_node
        # self.tail = new_node

    def print(self):
        cur_node = self.head

        while cur_node is not None:
            print(cur_node.data, end=" ")
            cur_node = cur_node.nxt


node = DLL(10)
node.add_to_tail(20)
node.add_to_tail(30)
node.add_to_tail(40)
node.print()
