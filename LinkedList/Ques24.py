def rotateDLL(self, head, p):
        if not head or p==0:
            return head
            
        length= 0
        temp= head
        while temp:
            length+=1
            temp=temp.next
            
        p= p%length
        if p==0:
            return head
            
        curr= head
        count= 1
        # stop at p-1 th node
        while count<p and curr:
            curr=curr.next
            count+=1

        newHead= curr.next
        newHead.prev= None
        curr.next= None
        
        tail=newHead
        while tail.next:
            tail= tail.next
            
        tail.next= head
        head.prev= tail
        
        
        return newHead
            
        