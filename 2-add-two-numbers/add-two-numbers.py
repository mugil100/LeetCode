# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2

        s1=""
        s2=""

        while p1 or p2:
            if p1:
                s1+= str(p1.val)
                p1 = p1.next
                print(s1)
            if p2:
                s2+= str(p2.val)
                p2 = p2.next
                print(s2)

        num1 = int(s1[::-1])
        num2 = int(s2[::-1])
        res_arr = list(str(num1+num2))
        dummy = ListNode(0)
        curr = dummy

        for x in res_arr[::-1]:
            curr.next = ListNode(int(x))
            curr = curr.next

        print(dummy.next)
        return dummy.next




            
        