from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        current_node = self.root

        while True:
            if value == current_node.value:
                return False
            elif value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                    return True
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    return True
                current_node = current_node.right

    def insertList(self, array):
        for value in array:
            self.insert(value)

    def inOrderTraversal(self):
        results = []

        def traversal(node):
            if node.left:
                traversal(node.left)
            results.append(node.value)
            if node.right:
                traversal(node.right)
        traversal(self.root)
        return results

    def BFS(self):
        queue = deque([self.root])
        results = []
        while queue:
            current_node = queue.popleft()
            if current_node:
                queue.append(current_node.left)
                queue.append(current_node.right)
                results.append(current_node.value)
        return results

    def maxDepth(self, node):
        if not node:
            return 0

        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)

        return 1 + max(left, right)

    def callMaxDepth(self):
        return self.maxDepth(self.root)

    def maxDepthBST(self):
        queue = deque([self.root])
        results = []
        depth = 0
        while queue:
            level = []
            for _ in range(len(queue)):
                current_node = queue.popleft()
                if current_node:
                    queue.append(current_node.left)
                    queue.append(current_node.right)
                    level.append(current_node.value)
            if level:
                results.append(level)
                depth += 1
        return results, depth

    def invert(self, node):
        if not node:
            return None

        temp = node.left
        node.left = node.right
        node.right = temp

        self.invert(node.left)
        self.invert(node.right)

    def invertTree(self):
        self.invert(self.root)

    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif not root or not subRoot or root.value != subRoot.value:
            return False
        return (self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right))

    def isSubTree(self, root, subRoot):
        if not subRoot:
            return True
        elif not root and subRoot != None:
            return False
        elif self.isSameTree(root, subRoot):
            return True
        return (self.isSubTree(root.left, subRoot) or self.isSubTree(root.right, subRoot))

    def kthSmallest(self, k):
        results = []

        def inOrder(node):
            if node.left:
                inOrder(node.left)
            results.append(node.value)
            if node.right:
                inOrder(node.right)
        inOrder(self.root)
        for _ in range(len(results)):
            return results[k-1]


values = [27, 14, 35, 10, 19, 31, 82]
bst = BinarySearchTree()
bst.insertList(values)
print(bst.BFS())
print(bst.inOrderTraversal())
print(bst.callMaxDepth())
print(bst.maxDepthBST())
print(bst.kthSmallest(3))
bst.invertTree()
print(bst.BFS())
bst.invertTree()
print(bst.BFS())
