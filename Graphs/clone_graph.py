"""
Clone Graph
Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.

Example 1:



Input: adjList = [[2],[1,3],[2]]

Output: [[2],[1,3],[2]]
Explanation: There are 3 nodes in the graph.
Node 1: val = 1 and neighbors = [2].
Node 2: val = 2 and neighbors = [1, 3].
Node 3: val = 3 and neighbors = [2].

Example 2:



Input: adjList = [[]]

Output: [[]]
Explanation: The graph has one node with no neighbors.

Example 3:

Input: adjList = []

Output: []
Explanation: The graph is empty.

Constraints:

0 <= The number of nodes in the graph <= 100.
1 <= Node.val <= 100
There are no duplicate edges and no self-loops in the graph.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, original_node):

        if not original_node:
            return None

        oldToNew = {}

        def dfs(node):
            # check if node is in the hashmap, cloned, return the clone
            if node in oldToNew:
                return oldToNew[node]

            # else, create a new node from the original node
            cloned_node = Node(node.val)

            # save the clone in the hashmap
            oldToNew[node] = cloned_node

            # Recursively clone all the neighbors
            for neighbor in node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))
            return cloned_node

        return dfs(original_node)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.neighbors = [node2]
node2.neighbors = [node1, node3]
node3.neighbors = [node2]

print(Solution().cloneGraph(node1))
