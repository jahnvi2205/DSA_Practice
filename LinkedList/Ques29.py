def segregate(self, head):
        if not head:
            return None
            
        curr= head
        one=None
        zero=None
        two=None
        one_head=None
        two_head=None
        zero_head=None
        
        while curr:
            val=curr.data
            nxt=curr.next
            curr.next=None
            
            if val==0:
                if zero is None:
                    zero_head=curr
                    zero= curr
                    
                else:
                    zero.next=curr
                    zero=zero.next
                    
            elif val==1:
                if one is None:
                    one_head=curr
                    one=curr
                   
                else:
                    one.next=curr
                    one=one.next
                   
            else:
                if two is None:
                    two_head= curr
                    two=curr

                else:
                    two.next= curr
                    two= two.next
            
            curr= nxt
            
            
        if zero_head:
            if one_head:
                zero.next= one_head
                if two_head:
                    one.next=two_head
            else:
                if two_head:
                    zero.next= two_head
            return zero_head
            
                
        elif one_head:
            if two_head:
                one.next=two_head
            
            return one_head
            
        return two_head
                
                
        
    