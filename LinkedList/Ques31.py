def mergeKLists(self, arr):
        heap=[]
        for i in range(0,len(arr)):
            heapq.heappush(heap, (arr[i].data, i, arr[i]))

        dummy= Node(0)
        tail = dummy
        
        while heap:
            _,i,node= heapq.heappop(heap)
            
            tail.next= node
            tail= tail.next
            
            if node.next:
                heapq.heappush(heap, (node.next.data,i, node.next ))
            
            
        return dummy.next