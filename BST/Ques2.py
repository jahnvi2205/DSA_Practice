def minval(self, root):
        curr= root
        while curr.left:
            curr=curr.left

        return curr

def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        elif key>root.val:
            root.right = self.deleteNode(root.right, key)

        elif key<root.val:
            root.left= self.deleteNode(root.left, key)

        else:
            # case 1: target has 0 child or 1 child
            if root.left==None:
                return root.right

            elif root.right ==None:
                return root.left

            # case 2: 2 children!!
            temp= self.minval(root.right)
            root.val= temp.val
            root.right= self.deleteNode(root.right, temp.val)

        return root