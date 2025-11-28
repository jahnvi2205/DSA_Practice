def height(self, root):
        # Remember that the return 0 and return -1 , gives out differnent things 
        # If you use 0, you would get the number of maximum "node" in the height
        # If you use -1, you would get the edges in the height of the tree, like in this case
        if not root:
            return -1
            
        leftheight= self.height(root.left)
        rightheight= self.height(root.right)
        
        return 1+ max(leftheight,rightheight)