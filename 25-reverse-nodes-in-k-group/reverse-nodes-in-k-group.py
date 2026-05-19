# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        curr = head
        while curr: #count the no of nodes
            curr = curr.next
            count+=1
        iter = count //k

        if iter <1:
            return None

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = end_node = head
        for _ in range(iter):
            for _ in range(k):
                end_node = end_node.next
            while curr.next != end_node:
                temp = curr.next
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp
            prev = curr
            curr = curr.next
        return dummy.next

        