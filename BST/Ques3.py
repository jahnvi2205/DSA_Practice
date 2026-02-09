def minValue(self, root):
        # recursive
        if not root.left:
            return root.data
        return self.minValue(root.left)
        
        # Iterative
        # if not root:
        #     return None
            
        # curr=root
        # while curr.left:
        #     curr= curr.left
            
        # return curr.data

def maxValue(self, root):
    #   recursive
    if not root.right:
        return root.data
    return self.maxValue(root.right)

    # iterative
    # if not root:
    #     return None
    
    # curr= root
    # while curr.right:
    #     curr= curr.right

    # return curr.data
    