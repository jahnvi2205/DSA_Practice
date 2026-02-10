def populateNext(self, root):
    self.prev= None
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        if self.prev:
            self.prev.next= node
        self.prev= node
        inorder(node.right)
            
    inorder(root)