def preorder_recursive(node):
    if not node:
        return
    
    print(node.data, end=" ")
    preorder_recursive(node.left)
    preorder_recursive(node.right)


def preorder_iterative(root):
    if not root:
        return
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        # Visit root
        print(node.data, end=" ")
        
        # Push right first (so left is processed first)
        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)



