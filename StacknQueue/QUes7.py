def reverse(self, s: str) -> str:
        stack=[]
        for i in s:
            stack.append(i)
            
        ans=""
        while stack:
            ans= ans+ stack.pop()
            
        return ans