def reverseKGroup(self, head, k):
    if head is None:
        return None
           
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
        