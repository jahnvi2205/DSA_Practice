def removeDuplicates(self, head):
        if not head:
            return None
            
        curr= head
        seen= set()
        seen.add(curr.data)
        
        while curr.next:
            if curr.next.data in seen:
                curr.next= curr.next.next
            else:
                curr= curr.next
                seen.add(curr.data)
                
        return head