"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head : return None
        curr = head
        #craete a new ll as a copy of the original ll
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = curr.next.next
        #merge the random pointers correctly
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        #seperate the clone from the original
        node = head
        copy_head = copy = head.next

        while node:
            node.next = copy.next
            node = node.next 
            if node:
                copy.next = node.next 
                copy = node.next
            
        return copy_head



