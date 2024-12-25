from typing import final


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
    def append(self, value): # 맨뒤에 붙이는 함수
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
    def display_all(self):
        cur = self.head
        while cur is not None:
            print(f"data {cur.data}")
            cur = cur.next

    def find(self, data):
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return cur
            else:
                cur = cur.next
        return None

    def insert(self, prev_data, data):
        cur = self.head
        new_node = Node(data)
        prev = self.find(prev_data)
        while cur is not None:
            if prev.data == cur.data:
                new_node.next = prev.next
                prev.next = new_node
                return
            cur = cur.next

    def remove(self, data):
        cur = self.head
        if cur.data == data:
            cur.next = cur.next.next
            return

        prev = None
        while cur is not None:
            if cur.data == data:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next


linked_list = LinkedList(5)
print(linked_list.head.data)
linked_list.append(3)
linked_list.append(6)
linked_list.append(7)
linked_list.display_all()

print("remove test")
linked_list.remove(3)
linked_list.display_all()
print(linked_list.find(7).data)

print("insert test")
linked_list.insert(5,3)
linked_list.display_all()
linked_list.insert(3,8)
linked_list.display_all()