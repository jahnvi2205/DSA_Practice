def countTriplets(self, n, sumi, arr):
        arr.sort()
        count=0
        for i in range(n-2):
            s= i+1
            e= n-1
            while s<e:
                curr= arr[i]+arr[s]+arr[e]
                if curr<sumi:
                    count+=(e-s)
                    s+=1
                elif curr>=sumi:
                    e-=1
                
        return count
            