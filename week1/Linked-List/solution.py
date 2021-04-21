class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

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
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self) -> list:
        answer = []
        curr = self.head
        while curr:
            answer.append(curr.data)
            curr = curr.next

        print(answer)
        return answer


    def insert(self, pos, newNode) -> bool:
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1: # 맨 앞일 경우
            newNode.next = self.head
            self.head = newNode
        else:
            if pos == self.nodeCount + 1: # 앞부터 찾지 말고 맨 뒤부터 할당
                prev = self.tail
            else:
                prev = self.getAt(pos - 1) # pos -1 노드를 찾는다.
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1: #맨 뒤일 경우
            self.tail = newNode
        self.nodeCount += 1
        return True


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        # 삭제 하려는 node가 맨 앞의 것 일때
        if pos == 1:
            curr = self.head
            self.head = self.head.next
        # 삭제하려는 node가 맨 마지막 일 때
        else:
            prev = self.getAt(pos-1)
            if pos == self.nodeCount:
                curr = prev.next
                self.tail = prev
                self.tail.next = None

            else:
                curr = self.getAt(pos)
                prev.next = curr.next
        self.nodeCount -= 1
        return curr

    def concat(self, L) -> None:
        self.tail.next = L.head
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

