def findmiddle(self, head):
        slow= head
        fast=head.next
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        return slow
        
    def merge(self, l1,l2):
        dummy= Node(-1)
        temp= dummy
        while l1 and l2:
            if l1.data < l2.data:
                temp.next= l1
                l1=l1.next
                
            else:
                temp.next= l2
                l2= l2.next
                
            temp=temp.next
            
        if l1:
            temp.next=l1
        if l2:
            temp.next=l2
            
        return dummy.next
            
        
    def mergeSort(self, head):
        if not head or not head.next:
            return head
            
        middle= self.findmiddle(head)
        right= middle.next
        middle.next=None
        left= head
        
        left= self.mergeSort(left)
        right= self.mergeSort(right)
        
        return self.merge(left,right)
        