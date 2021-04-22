class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s

    def getAt(self, pos) -> Node:
        if pos < 0 or pos > self.nodeCount:
            return None
        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self) -> list:
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)

        return result

    def insertAfter(self, prev, newNode) -> bool:
        newNode.next = prev.next
        # prev가 tail 일경우
        if prev.next is None:
            self.tail = newNode

        prev.next = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode) -> bool:
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        # 연결 리스트가 완전비 비어 있는 경우
        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)

        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        # prev가 마지막 일때
        if prev.next is None:
            self.nodeCount -= 1
            return None


        curr = prev.next
        # 리스트 맨끝의 node를 삭제 할때 -> tail 조정 필요
        if curr.next is None:
            prev.next = None
            self.tail = prev

        prev.next = curr.next
        self.nodeCount -= 1
        return curr.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos-1)
        return self.popAfter(prev)

    def concat(self, L) -> None:
        self.tail.next = L.head.next
        # tail이 존재하는 경우 만 tail을 연결
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount


if __name__ == "__main__":
    a = Node(12)
    b = Node(24)
    c = Node(36)
    L = LinkedList()
    L.insert(1, a)
    L.insert(2, b)
    L.insert(3, c)
