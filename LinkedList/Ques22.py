def count_triplets(self, head, target):
    if not head:
        return 0

    tail= head
    while tail.next:
        tail= tail.next

    count= 0
    i= head
    
    while i:
        left= i.next
        right= tail

        while left and right and left!=right and right.next !=left:
            currSum= i.data+ left.data+ right.data
            if currSum==target:
                count+=1
                left= left.next
                right = right.prev

            elif currSum <target:
                left=left.next
            else:
                right= right.prev

        i=i.next

    return count
