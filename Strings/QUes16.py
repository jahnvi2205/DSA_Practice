 def isValid(self, s: str) -> bool:
        temp=''
        for i in s:
            if i in '({[':
                temp+= i
            
            elif temp!='':
                if i=="}" and temp[-1]=='{':
                    temp= temp[:-1]
                elif i==")" and temp[-1]=='(':
                    temp= temp[:-1]
                elif i==']' and temp[-1]=='[':
                    temp= temp[:-1]
                else:
                    return False

            else:
                return False
        
        if len(temp)==0:
            return True
        return False
        

        

        