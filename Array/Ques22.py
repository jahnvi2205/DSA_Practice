def factorial(self, n):
        ans=1
        for i in range(2,n+1):
            ans *= i
        
        l=[]
        for i in range(len(str(ans))):
            l.append(int(str(ans)[i]))
            
        return l