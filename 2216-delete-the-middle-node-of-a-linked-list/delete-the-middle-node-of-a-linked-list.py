# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr  = head
        count = 0
        if not head:
            return None
        #find the len of the tree
        while curr:
            count+=1
            curr = curr.next
        mark = count //2
        #iterate thru the ll
        if count==1:
            return None
        x=1
        curr = head
        while x!=mark:
            curr = curr.next
            x+=1
        #detach
        temp = curr.next
        curr.next = curr.next.next
        temp.next = None
        return head



        