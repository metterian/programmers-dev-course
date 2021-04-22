#%%
class Node:
    def __init__(self, item) -> None:
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        # 왼쪽 자식 노드가 존재 할때 사이즈를 구하고, 없으면 0 을 반환 한다(종료 조건)
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return max(l, r) + 1


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()

        return traversal

    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal

    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal

class BinaryTree:
    def __init__(self, r) -> None:
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []

#%%
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



    print ("Height of tree is %d" %(root.depth()))
    print ("In-Order: ", " -> ".join(root.inorder()))
    print ("Pre-Orderl: ", " -> ".join(root.preorder()))
    print ("post-Orderl: ", " -> ".join(root.postorder()))
# %%
