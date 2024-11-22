"""
Same Binary Tree
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Example 1:



Input: p = [1,2,3], q = [1,2,3]

Output: true
Example 2:



Input: p = [4,7], q = [4,null,7]

Output: false
Example 3:



Input: p = [1,2,3], q = [1,3,2]

Output: false
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):

        # Base case: if both nodes are None, the trees are identical at this point
        if not p and not q:
            return True

        # If one of the nodes is None and the other is not, the trees are not identical
        elif not p or not q or p.value != q.value:
            return False

        # Check if the values of the current nodes are equal, and recursively check the left and right subtrees
        self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
