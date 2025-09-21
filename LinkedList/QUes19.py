def deleteNode(self, head, key):
        if not head:
            return None
            
        if head.next==head and head.data==key:
            return None
            
        # delete at start
        if key==head.data:
            curr=head
            while curr.next!= head:
                curr=curr.next
                
            curr.next=head.next
            head=head.next
            return head
            
            
        curr=head
        while curr.next!= head:
            if curr.next.data == key:
                curr.next=curr.next.next
                return head
            curr=curr.next
        
        return head
        