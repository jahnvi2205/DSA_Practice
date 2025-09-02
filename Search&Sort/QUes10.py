def findPair(self, arr: List[int], x: int) -> int:
        arr.sort()
        s= 0
        e= 1
        while s<len(arr) and e<len(arr):
            diff= arr[e]-arr[s]
            if diff==x and s!=e:
                return True
            elif diff>x:
                s+=1
            else:
                e+=1
        return False