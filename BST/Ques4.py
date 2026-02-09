def minvalue(self,root):
        curr= root
        while curr.left:
            curr= curr.left
        return curr
        
    def maxvalue(self,root):
        curr= root
        while curr.right:
            curr= curr.right
        return curr
            
    def findPreSuc(self, root, key):
        pre= None
        suc= None
        
        curr= root
        while curr:
            if key<curr.data:
                suc= curr
                curr= curr.left
            elif key>curr.data:
                pre= curr
                curr= curr.right
                
            else:
                if curr.left:
                    pre= self.maxvalue(curr.left)
                    
                if curr.right:
                    suc= self.minvalue(curr.right)
                break
            
        return [pre, suc]
        
        