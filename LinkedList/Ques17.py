def splitList(self, head):
        if not head:
            return None, None
            
        slow= head
        fast= head
        
        while fast.next!= head and fast.next.next != head:
            slow=slow.next
            fast=fast.next.next
            
        #   If even number of nodes, move fast to last node
        if fast.next.next == head:
            fast = fast.next
        
        head1= head
        head2= slow.next
        
        slow.next=head1
        fast.next=head2
        
        return head1,head2