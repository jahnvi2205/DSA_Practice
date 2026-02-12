def postorder_recursive(node):
    if not node:
        return
    postorder_recursive(node.left)
    postorder_recursive(node.right)
    print(node.data,end=" ")

def postorder_itrative(node):
    # Stack1 we WANT: Root → Right → Left
    # stack2 = stack1.reverse = postorder

    stack1= [node]
    stack2= []

    while stack1:
        curr= stack1.pop()
        stack2.append(curr)
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)

    while stack2:
        curr=stack2.pop()
        print(curr.data,end=" ")