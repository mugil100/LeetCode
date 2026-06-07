"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def findNode(node):

            while node:
                if node.left:
                    return node.left
                if node.right:
                    return node.right
                node = node.next#why do i do this
            return None

        def dfs(node):
            if not node:
                return None
            if node.left and node.right:
                node.left.next = node.right
            if node.right:
                node.right.next = findNode(node.next)
            if node.left and not node.right:
                node.left.next = findNode(node.next)

            dfs(node.right)
            dfs(node.left)
        dfs(root)
        return root
