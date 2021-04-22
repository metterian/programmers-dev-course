#%%
class CircularQueue:
    def __init__(self, n) -> None:
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1

    # 현재 큐 길이 반환
    def size(self):
        return self.count

    # 큐가 꽉 차 있는가?
    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError("Queue is full")

        self.rear =  (self.rear + 1) % self.maxCount
        print("rear: ", self.rear)
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.count is self.maxCount:
            raise IndexError("Queue is full")

        self.front = (self.front +1) % self.maxCount
        print("front: ", self.front)
        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):
        if not self.data:
            raise IndexError("Queue is empty")
        return self.data[self.front]


queue = CircularQueue(6)
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
queue.enqueue('D')

print(queue.dequeue())
print(queue.dequeue())
# queue.enqueue('E')
# queue.enqueue('F')
queue.data

# %%
