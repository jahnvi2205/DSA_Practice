def divide(self, head):
        
        even= None
        odd=None
        head_even= None
        head_odd= None
        curr= head
        
        while curr:
            val=curr.data
            nxt=curr.next
            curr.next=None
            
            if val&1:
                if not odd:
                    odd= curr
                    head_odd= curr
                    
                else:
                    odd.next =curr
                    odd= odd.next
                    
            else:
                if not even:
                    even= curr
                    head_even= curr
                  
                else:
                    even.next=curr
                    even=even.next
            
            curr=nxt
            
        if head_even:
            if head_odd:
                even.next= head_odd
                    
            return head_even
                
        return head_odd
            
        