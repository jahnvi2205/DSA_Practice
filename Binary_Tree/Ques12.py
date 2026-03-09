from collections import deque
class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return []
            
        result=[]
        hd_map= {}
        queue= deque()
        queue.append((root,0))
        
        while queue:
            node, level= queue.popleft()
            
            hd_map[level]= node.data
            
            if node.left:
                queue.append((node.left,level-1))
                
            if node.right:
                queue.append((node.right,level+1))
                
        for level in sorted(hd_map.keys()):
            result.append(hd_map[level])
            
        return result
        