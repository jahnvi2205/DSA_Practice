def reverseKGroup(self, head, k):
        node= head
        count= 0
        while node and count<k:
            node= node.next
            count+=1
            
        if count<k and head is None:
            return head
            
        prev= None
        curr= head
        nex= None
        count=0
        
        while curr and count<k:
            nex= curr.next
            curr.next=prev
            prev= curr
            curr= nex
            count+=1
        
        head.next= self.reverseKGroup(curr, k)
        
        return prev
        