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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def find(node):
            while node:
                if node.left:
                    return node.left
                if node.right:
                    return node.right
                node = node.next
            return None
        def dfs(node):

            if not node:
                return None
            if node.left and node.right:
                node.left.next = node.right
            if node.right:
                node.right.next = find(node.next)
            if node.left and not node.right:
                node.left.next = find(node.next)

            dfs(node.right)
            dfs(node.left)

        dfs(root)
        return root
        