def removeLoop(self, head):
        slow= head
        fast= head
        
        # Step 1: Detect cycle using Floyd’s Algorithm
        while fast and fast.next is not None:
            slow= slow.next
            fast= fast.next.next
            if slow==fast:
                break
            
        else: 
            return False
            
        # Step 2: Find start of the loop
        slow= head
        while slow!= fast:
            slow=slow.next
            fast=fast.next
         
        # Step 3: Find the node before the loop start and break it   
        ptr=slow
        while ptr.next!=slow:
            ptr=ptr.next
            
        ptr.next=None
        return True
        
