def findIntersection(self,head1,head2):
        curr1= head1
        curr2= head2
        Dummy= Node(0)
        curr3= Dummy
        
        while curr1 and curr2:
            if curr1.data== curr2.data:
                curr3.next= Node(curr1.data)
                curr3= curr3.next
                curr2= curr2.next
                curr1= curr1.next
            elif curr1.data> curr2.data:
                curr2= curr2.next
                
            else:
                curr1= curr1.next
            
            
        return Dummy.next