# python实现链表，使其能完成增删改查
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, n):
        new_node = Node(n)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, n):
        if self.head is None:
            return
        if self.head.key == n:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.key == n:
                current.next = current.next.next
                return
            current = current.next

    def change(self, pos, n):
        if self.head is None:
            return
        current = self.head
        position = 0
        while current:
            if position == pos:
                current.key = n
                return
            current = current.next
            position += 1

    def search(self, value):
        current = self.head
        while current:
            if current.key == value:
                return True
            current = current.next
        return False

    # 打印链表
    def display(self):
        current = self.head
        while current:
            print(current.key, end = " -> ")
            current = current.next
        print("None")