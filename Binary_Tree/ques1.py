def levelOrder(self, root):
        # code here
        if not root:
            return []
            
        result=[]
        q= deque([root])
        
        while q:
            level_size= len(q)
            level=[]
            
            for _ in range(level_size):
                node= q.popleft()
                level.append(node.data)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                
            result.append(level)    
                
        return result
            