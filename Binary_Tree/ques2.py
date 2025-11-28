def reverseLevelOrder(self,root):
        if not root:
            return []
            
        q= deque([root])
        stack= []
        ans=[]
        
        while q:
            node= q.popleft()
            stack.append(node.data)
            
            # BFS order should be reversed (right→left) So that after stack reversal you get left→right

            if node.right:
                q.append(node.right)
                
            if node.left:
                q.append(node.left)
                
            
        while stack:
            ans.append(stack.pop())
            
        return ans