def isCircular(self, head):
        if not head:
            return False
        slow=head
        fast=head
        
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            
            if fast== slow:
                return True
            
        return False