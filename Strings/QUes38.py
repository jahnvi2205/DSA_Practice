def remove(self, s, index, prev, result):
        if index>= len(s):
            return "".join(result)
            
        if s[index]!= prev:
            result.append(s[index])
            
        return self.remove(s,index+1,s[index],result)
        
            
    def removeConsecutiveCharacter(self, s):
        # code here
        if not s:
            return None
        return self.remove(s,0, None, [])
        