def binaryTreeToBST(self, root):
        arr = []
        
        # Step 1: Store inorder
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            arr.append(node.data)
            inorder(node.right)
        
        inorder(root)
        
        # Step 2: Sort
        arr.sort()
        
        # Index for sorted array
        i = 0
        
        # Step 3: Replace values
        def fill(node):
            nonlocal i
            
            if not node:
                return
            
            fill(node.left)
            node.data = arr[i]
            i += 1
            fill(node.right)
        
        fill(root)
        
        return root