class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.root = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.root = Node(data)
            print(self.root)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    # Inorder traversal (DFS)
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    # PreOrder traversal (DFS)
    #  Root -> Left -> Right
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res

    # Postorder traversal (DFS)
    # Left -> RIght -> Root
    def postorderTraversal(self, root):
        res = []
        if root:
            res = res + self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res

    # levelorder traversal (Breadth-first Search) 0n
    def BFS(self, root):
        queue = []
        res = []
        queue.append(root)

        while queue:
            current_node = queue.pop(0)
            if current_node:
                res.append(current_node.data)
                queue.append(current_node.left)
                queue.append(current_node.right)
        return res

    # levelorder traversal (Breadth-first Search) 0n4
    def levelorderTraversal(self, node):
        queue = []
        res = []
        # enqueue root and initialize height
        queue.append(node)
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                # print(node)
                # enqueue left child
                if node:
                    level.append(node.data)
                    queue.append(node.left)
                    queue.append(node.right)
                    # print(len(queue))

            if level:
                res.append(level)

        return res


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(82)
# root.insert(42)
# root.printTree()
# print(root)


# print(newGraph.levelorderTraversal('A'))
# print(root.inorderTraversal(root))
# print(root.preorderTraversal(root))
# print(root.postorderTraversal(root))
# print(root.levelorderTraversal(root))
print(root.BFS(root))
print(root.preorderTraversal(root))
print(root.postorderTraversal(root))
print(root.inorderTraversal(root))
print(root.levelorderTraversal(root))
