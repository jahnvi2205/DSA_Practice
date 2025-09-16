def isBalanced(self, s):
        stack=[]
        for i in s:
            if i in '[{(':
                stack.append(i)
            elif stack:
                if i==')' and stack[-1]=='(':
                    del stack[-1]
                elif i==']' and stack[-1]=='[':
                    del stack[-1]
                elif i=='}' and stack[-1]=='{':
                    del stack[-1]
                else:
                    return False
            else:
                return False
        
        if not stack:
            return True
            
        return False
                