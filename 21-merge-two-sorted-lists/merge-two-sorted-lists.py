class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to act as the start of the merged list
        dummy = ListNode(-1)
        curr = dummy
        
        # 2. Loop while BOTH lists have nodes remaining
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1  # Splice the actual node, don't create a new one
                list1 = list1.next # Move list1 pointer forward
            else:
                curr.next = list2  # Splice list2 node
                list2 = list2.next # Move list2 pointer forward
            
            curr = curr.next       # Crucial: Move your tracking pointer forward!
            
        # 3. Attach the remaining nodes of whichever list isn't empty
        curr.next = list1 if list1 else list2
        
        # 4. Return the head of the sorted list (skipping the dummy node)
        return dummy.next