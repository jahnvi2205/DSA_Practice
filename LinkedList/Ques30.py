def cloneLinkedList(self, head):
        if not head:
            return None
            
            # Step 1: Insert copy nodes
        curr= head
        while curr:
            dup= Node(curr.data)
            dup.next=curr.next
            curr.next=dup
            curr=curr.next.next
            
            
            # Step 2: Assign random pointers
        curr=head
        while curr:
            if curr.random:
                curr.next.random= curr.random.next
            else:
                curr.random= None
            curr= curr.next.next
            
            
            # Step 3: Separate the lists
        copy_head= head.next
        curr= head
        while curr:
            copy= curr.next
            curr.next=copy.next
            if copy.next:
                copy.next=copy.next.next
            curr=curr.next
                
        
        return copy_head