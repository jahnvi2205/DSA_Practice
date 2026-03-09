from collections import deque
class Solution:
    def zigZagTraversal1(self, root):
        if not root:
            return []
            
        result=[]

        current_level=[]
        next_level=[]
        
        current_level.append(root)
        left_right=True
        
        while current_level:
            node= current_level.pop()
            result.append(node.data)
            
            if left_right:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
            else:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
                    
            if not current_level:
                current_level, next_level= next_level, current_level
                left_right= not left_right
                
        return result
    

    def zigZagTraversal2(self, root):      
        if not root:
            return []
            
        result=[]
        level=1
        queue= deque([root])
        
        while queue:
            level_size=len(queue)
            temp=[]
            
            for _ in range(level_size):
                node= queue.popleft()
                temp.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                
            if level%2 == 0:
                temp.reverse()
                
            result.extend(temp)
            level+=1
            
        return result      