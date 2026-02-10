
def Bst(pre, size) -> Node:
    i= 0
    def build(low, high):
        nonlocal i
        if i == size:
            return None
        val= pre[i]
        if val<=low or val>=high:
            return None
            
        node= Node(val)
        i+=1
        
        node.left= build(low,val)
        node.right= build(val, high)
        
        return node
        
    return build(float('-inf'), float('inf'))