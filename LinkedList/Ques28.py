def merge(self, a, b):
        if not a :
            return b
        if not b :
            return a
        
        if a.data< b.data:
            a.bottom= self.merge(a.bottom, b)
            return a
            
        else:
            b.bottom = self.merge(a, b.bottom )
            return b
        
        
    
def flatten(self, root):
    if not root or not root.next:
        return root
            
    root.next= self.flatten(root.next)
    root= self.merge(root,root.next)
        
    return root