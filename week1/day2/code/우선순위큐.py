from doublylinkedlist import Node, DoublyLinkedList

class PriorityQueue:

    def __init__(self):
        self.queue = DoublyLinkedList()


    def size(self):
        return self.queue.getLength()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head
        while curr.next != self.queue.tail and curr.next.data > newNode.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data


if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.enqueue(12)
    myQueue.enqueue(1)
    myQueue.enqueue(14)
    myQueue.enqueue(7)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.dequeue())
