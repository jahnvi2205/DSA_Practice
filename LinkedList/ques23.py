import heapq

def sorted_dll(self, head, k):
    if not head:
        return head

    heap= []

    curr= head
    for _ in range(k+1):
        if not curr:
            break

        heapq.heappush(heap, (curr.data,curr))
        curr = curr.next

    new_head= None
    last= None 

    while heap:
        _, node= heapq.heappop(heap)

        if not new_head:
            new_head= node
            last= new_head
            new_head.prev= None 

        else:
            last.next= node
            node.prev= last
            last= node

        if curr:
            heapq.heappush(heap,(curr.data,curr))
            curr=  curr.next

    last.next= None
    return new_head
































