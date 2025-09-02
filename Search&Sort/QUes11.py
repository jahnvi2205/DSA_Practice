def fourSum(self, arr, target):
        arr.sort()
        n=len(arr)
        l=[]
        
        for i in range(n):
            if i>0 and arr[i]== arr[i-1]:
                continue
            
            for j in range(i+1,n):
                if j>i+1 and arr[j]== arr[j-1]:
                    continue
                
                s= j+1
                e= n-1
                while s<e:
                    if arr[i]+arr[j]+arr[s]+arr[e]== target:
                        l.append([arr[i], arr[j], arr[s], arr[e]])
                        s+=1
                        e-=1
                        while s<e and arr[s]==arr[s-1]:
                            s+=1
                        while s<e and arr[e]==arr[e+1]:
                            e-=1
                            
                    elif arr[i]+arr[j]+arr[s]+arr[e]> target:
                        e-=1
                    else:
                        s+=1
                    
                    
        return l
                
        