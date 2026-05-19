class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node that points to the head
        dummy = ListNode(0, head)
        
        # 'pred' (predecessor) will stay behind the chunk of duplicates we are inspecting
        pred = dummy
        
        while head:
            # 2. If it's the start of a duplicate sequence
            if head.next and head.val == head.next.val:
                # Move 'head' to the end of the duplicate sequence
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skip all duplicates by linking pred.next to the node AFTER the duplicates
                pred.next = head.next 
            else:
                # 3. No duplicate detected, safe to move 'pred' forward
                pred = pred.next
                
            # Move head forward for the next iteration
            head = head.next
            
        return dummy.next