class Solution:
    def kthSmallest(self, root, k): 
        # code here
        self.count = 0
        self.ans = -1

        def inorder(node):
            if not node or self.count >= k:
                return

            # Left
            inorder(node.left)

            # Root
            self.count += 1
            if self.count == k:
                self.ans = node.data
                return

            # Right
            inorder(node.right)

        inorder(root)
        return self.ans
        