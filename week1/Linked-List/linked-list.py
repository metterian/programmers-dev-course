class Node:
    def __init__(self, item) -> None:
        self.data = item # item을 받아서 data에 저장
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos <= 0 or pos > self.nodeCount: # 찾는 위치가 불가능 할 경우
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr
