def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        if not head:
            return []
            
        start= head
        end= head
        result= list()
        
        while end.next:
            end= end.next
            
        while start and end and start.data< end.data:
            sumi= start.data+ end.data
            if sumi== target:
                result.append((start.data,end.data))
                start=start.next
                end=end.prev
                
            elif sumi>target:
                end=end.prev
            else:
                start=start.next
                
        return result
                