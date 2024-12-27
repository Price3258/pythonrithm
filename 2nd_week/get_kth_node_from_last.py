# Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.

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

    def get_length(self):
        cur = self.head
        length = 0
        while cur is not None:
            cur = cur.next
            length +=1
        return length


    def get_kth_node_from_last(self, k):

        cur = self.head
        length =self.get_length()

        if length - k < 0:
            return Node(None)

        for i in range(length):
            if i == length -k:
                return cur
            cur = cur.next
        return None


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
# linked_list.append(9)
# linked_list.append(10)
# linked_list.append(11)

print(linked_list.get_length())
print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!