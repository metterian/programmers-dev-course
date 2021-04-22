class Node:
    def __init__(self, key, data) -> None:
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()

        traversal.append(self) # self의 data를 입력 하는 것이 아니라 노드(self) 들의 리스트를 입력한다

        if self.right:
            traversal += self.right.inorder()

        return traversal

    def min(self):
        # 계속해서 왼쪽만 쫒아가면 가장 작은 값을 만나게 된다.
        if self.left:
            return self.left.min()
        # 왼쪽으로 더 이상 갈 수 없므면 자기 자신이 최소값임
        else:
            return self

    def max(self):
        pass

    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent

    def insert(self, key, data):
        if key < self.key:
            if self.left:
                return self.left.insert(key, data)
            else:
                new = Node(key, data)
                self.left = new
        elif self.key < key:
            if self.right:
                return self.right.insert(key, data)
            else:
                new = Node(key, data)
                self.right = new
        # self 노드와 같은 것 -> 중복을 존재 하지 않다고 가정
        else:
            raise KeyError




class BinSearchTree:
    def __init__(self) -> None:
        self.root = None

    def inorder(self):
        if self.root:
            return self.root.inroder()
        else:
            return []

    def min(self):
        if self.root:
            return self.root.min()
        else:
            return None

    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)
