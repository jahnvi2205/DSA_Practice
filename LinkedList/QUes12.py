def intersectPoint(self, head1, head2):
        curr1= head1
        curr2= head2
        
        while curr1!= curr2:
            curr1= curr1.next
            curr2= curr2.next
            
            if curr1== curr2:
                return curr2
                
            if curr1== None:
                curr1=head2
                
            if curr2== None:
                curr2= head1
                
        return curr2