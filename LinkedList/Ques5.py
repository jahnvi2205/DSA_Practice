def cycleStart(self, head):
        slow=head
        fast= head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                break
            
        if slow==fast:
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
                
            return slow.data
            
        return -1