def rightView(self, root):
        result=[]
        def helper(root,level):
            if not root:
                return
            
            if len(result)==level:
                result.append(root.data)
                
            helper(root.right,level+1)
            helper(root.left,level+1)
        
        
        
        helper(root,0)
        return result