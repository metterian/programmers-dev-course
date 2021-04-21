class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

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

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr

    def traverse(self) -> list:
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)

        return result

    def reverse(self) -> list:
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)

        return result

    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode) -> bool:
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        if prev.next.next is None:
            self.nodeCount -= 1
            return None

        curr = prev.next
        next = curr.next

        data = curr.data
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return data


    def popBefore(self, next):
        if next.prev.prev is None:
            self.nodeCount -= 1
            return None

        curr = next.prev
        prev = curr.prev
        data = curr.data

        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos-1)
        return self.popAfter(prev)

    def concat(self, L) -> None:
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount


if __name__ == "__main__":
    a = Node(62)
    b = Node(85)
    c = Node(43)
    L = DoublyLinkedList()
    L.insertAt(1, a)
    L.insertAt(2, b)
    L.insertAt(3, c)
