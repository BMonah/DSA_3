class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        current_node = self.root
        while (True):
            if new_node.value == current_node.value:
                return False
            if new_node.value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return True
                current_node = current_node.left
            if new_node.value > current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                current_node = current_node.right

    def insertList(self, value):
        for item in value:
            self.insert(item)

    def inorder(self):
        results = []
        current_node = self.root

        def checkorder(current_node):
            if not self.root:
                return None
            if current_node.left:
                checkorder(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                checkorder(current_node.right)

        checkorder(current_node)
        return results

    def postorder(self):
        results = []
        current_node = self.root

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(current_node)
        return results

    def preorder(self):
        results = []
        current_node = self.root

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
        traverse(current_node)
        return results

    def BFS_levelorder(self):
        queue = []
        results = []
        queue.append(self.root)
        while queue:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.right:
                queue.append(current_node.left)
            if current_node.left:
                queue.append(current_node.right)
        return results

    def BFS_Depth(self):
        queue = []
        current_node = self.root
        queue.append(current_node)
        results = []
        level = []
        count = 0
        while queue:
            for item in range(len(queue)):
                current_node = queue.pop(0)
                results.append(current_node.value)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            level.append(results)
            results = []
            count += 1
        print(len(level[0]))

        # get maximum
        maximum = 0
        for item in range(len(level)):
            maxi = len(level[item])
            maximum = max(maximum, maxi)
        return level, count, maximum

    def find_kth(self, kth):
        results = []
        current_node = self.root

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)
        traverse(current_node)
        if kth-1 not in range(len(results)):
            return None
        kth = results[kth-1]
        return kth

    def validate_tree(self):
        results = []
        current_node = self.root

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)
        traverse(current_node)
        for i in range(1, len(results)):
            if results[i] <= results[i-1]:
                return False
        return True

    def depth_DFS(self):
        current_node = self.root

        def traverse(current_node):
            if current_node is None:
                return 0

            left_depth = traverse(current_node.left)
            right_depth = traverse(current_node.right)
            return 1 + max(left_depth, right_depth)
        return traverse(current_node)

    def invert(self):
        current_node = self.root

        def invert(current_node):
            if current_node is None:
                return 0
            temp = current_node.left
            current_node.left = current_node.right
            current_node.right = temp
            invert(current_node.left)
            invert(current_node.right)

        invert(current_node)


nodes = [27, 14, 35, 10, 19, 31, 82]
BSTree = BST()
BSTree.insertList(nodes)
print(BSTree.inorder())
print(BSTree.postorder())
print(BSTree.preorder())
BSTree.invert()
print(BSTree.BFS_levelorder())
print(BSTree.BFS_Depth())
print(BSTree.find_kth(3))
print(BSTree.validate_tree())
print(BSTree.depth_DFS())
print(BSTree.inorder())
