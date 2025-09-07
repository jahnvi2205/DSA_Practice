def moveToFront(self, head : Optional['Node']) -> Optional['Node']:
        curr=head
        while curr.next.next:
            curr=curr.next
            
        temp= curr.next
        temp.next= head
        curr.next=None
        
        return temp