def inorder_recurse(node):
    if not node:
        return
    inorder_recurse(node.left)
    print(node.data, end=" ")
    inorder_recurse(node.right)

def inorder_iterative(root):
    stack = []
    curr = root
    
    while curr or stack:
        
        # Go to leftmost node
        while curr:
            stack.append(curr)
            curr = curr.left
        
        # Process node
        curr = stack.pop()
        print(curr.data, end=" ")
        
        # Move to right subtree
        curr = curr.right