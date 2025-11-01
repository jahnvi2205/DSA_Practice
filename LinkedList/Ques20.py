def reverse(self, head):
        if not head:
            return None
            
        prev_node= head.prev
        curr= head
        next_node= head.next
        
        while next_node:
            curr.prev= next_node
            curr.next= prev_node
            
            prev_node= curr
            curr= next_node
            next_node= next_node.next
            
        
        curr.prev= next_node
        curr.next= prev_node
        
        return curr