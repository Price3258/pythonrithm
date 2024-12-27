class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_value(self):
        cur = self.head
        value = ''
        while cur is not None:
            value += str(cur.data)
            cur = cur.next
        return int(value)



def get_linked_list_sum(first, second):
    # 구현해보세요!

    return first.get_value() + second.get_value()


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2)) # 1032 가 되어야 함. 