# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        prev = dummy = ListNode(0)
        prev.next = head
        head2 = dummy2 = ListNode(0)
        while prev.next:
            if prev.next.val < x:
                prev = prev.next

            else:
                temp = prev.next
                prev.next = prev.next.next
                dummy2.next = temp
                dummy2 = temp
                temp.next = None
                
        prev.next = head2.next

        return dummy.next


        