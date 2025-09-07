def removeDuplicates(head):
    curr=head
    while curr and curr.next:
        if curr.next and curr.data== curr.next.data:
            curr.next=curr.next.next
        else:
            curr=curr.next