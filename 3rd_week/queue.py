class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None  # 큐의 앞쪽(가장 먼저 삽입된 노드)
        self.tail = None  # 큐의 끝쪽(가장 마지막으로 삽입된 노드)

    def enqueue(self, value):
        """큐의 끝에 값을 추가"""
        new_node = Node(value)
        if self.is_empty():
            # 큐가 비어있으면 head와 tail이 새 노드를 가리킴
            self.head = new_node
            self.tail = new_node
        else:
            # 새 노드를 tail 뒤에 연결하고 tail을 새 노드로 이동
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        """큐의 앞쪽에서 값을 제거"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        # head를 다음 노드로 이동
        removed_value = self.head.data
        self.head = self.head.next
        # 큐가 비어 있으면 tail도 None으로 설정
        if self.head is None:
            self.tail = None
        return removed_value

    def peek(self):
        """큐의 앞쪽 값을 반환"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.head.data

    def is_empty(self):
        """큐가 비어 있는지 확인"""
        return self.head is None


# 테스트
queue = Queue()

# 큐에 값 추가
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.peek())  # 출력: 1
print(queue.dequeue())  # 출력: 1
print(queue.dequeue())  # 출력: 2
print(queue.is_empty())  # 출력: False
print(queue.dequeue())  # 출력: 3
print(queue.is_empty())  # 출력: True
