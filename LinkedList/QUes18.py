def reverse(self,head):
        prev= None
        curr=head
        
        while curr:
            nex=curr.next
            curr.next= prev
            prev= curr
            curr=nex
            
        return prev
        
        
    def isPalindrome(self, head):
        # code here
        if not head or not head.next:
            return True
            
        mid= head
        end= head
        
        while end and end.next:
            end= end.next.next
            mid= mid.next
            
        if end:     #for odd
            mid=mid.next
            
        first=head
        second= self.reverse(mid)
        
        while second:
            if first.data != second.data:
                return False
                
            first= first.next
            second= second.next
                
        return True
        
        
        