class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        traversal = []
        queue = ArrayQueue()
        if self.root:
            queue.enqueue(self.root)
        while not queue.isEmpty():
            now = queue.dequeue()
            traversal.append(now.data)
            if now.left:
                queue.enqueue(now.left)
            if now.right:
                queue.enqueue(now.right)

        return traversal


if __name__ == '__main__':
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.left.left.left = Node('H')

    root.right.right = Node('G')
    root.right.left = Node('F')
    root.right.left.right = Node('J')

    tree = BinaryTree(root)

    print("BFS: ", " -> ".join(tree.bft()))
    # print(tree.bft())
