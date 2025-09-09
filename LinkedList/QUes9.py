def reverse(self,head):
        prev= None
        curr= head
        while curr:
            nex= curr.next
            curr.next= prev
            prev= curr
            curr= nex
        
        return prev
        
        
        
    def addOne(self,head):
        temp= self.reverse(head)
        curr= temp
        
        curr.data+=1
        carry= curr.data//10
        curr.data=curr.data %10
        
        
        while curr.next and carry:
            curr=curr.next
            curr.data+=carry
            carry= curr.data//10
            curr.data= curr.data %10
            
        if carry:
            curr.next= Node(carry)
            
        return self.reverse(temp)        