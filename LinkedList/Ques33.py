def reverse(self, head):
        prev= None
        curr=head
        
        while curr:
            nxt= curr.next
            curr.next=prev
            prev=curr
            curr= nxt
            
        return prev
            
    def compute(self,head):
        if not head or not head.next:
            return head
            
        head= self.reverse(head)
        max_val= head.data
        curr= head
        
        while curr and curr.next:
            if curr.next.data < max_val:
                curr.next= curr.next.next
                
            else:
                curr= curr.next
                max_val= curr.data
                
                
        head= self.reverse(head)
        return head
            
        