def reverse(self,head):
        prev= None
        curr= head
        
        while curr:
            nex= curr.next
            curr.next=prev
            prev= curr
            curr=nex
            
        return prev
            
             
    def addTwoLists(self, head1, head2):
        temp1= self.reverse(head1)
        temp2= self.reverse(head2)
        
        curr1= temp1
        curr2= temp2
        carry=0
        
        New= Node(0)
        curr3= New
        
        while curr1 or curr2 or carry:
            total=carry
            
            if curr1:
                total+=curr1.data
                curr1=curr1.next
            if curr2:
                total+=curr2.data
                curr2=curr2.next
            
            carry=total//10
            curr3.next= Node(total%10)
            curr3= curr3.next
            
        result= self.reverse(New.next)
            
        while result and result.data==0 and result.next:
            result=result.next
                
        return result