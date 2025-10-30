def reverseList(self, head):
    # Iterative method
    curr= head
    prev= None
    next= None
            
    while curr:
        next= curr.next
        curr.next= prev
        prev=curr
        curr= next
                
    return prev


def reverseList(self, head):
        # Using stack
        stack= []
        temp = head
        
        while temp.next is not None:
            stack.append(temp)
            temp=temp.next
            
        head=temp
        
        while stack:
            temp.next= stack.pop()
            temp=temp.next
          
        temp.next= None
        
        return head
        