class Solution:
    def kthLargest(self,root, k):
        #your code here
        self.count = 0
        self.ans = -1

        def reverse_inorder(node):
            if not node or self.count >= k:
                return

            # Go to right subtree first
            reverse_inorder(node.right)

            # Visit current node
            self.count += 1
            if self.count == k:
                self.ans = node.data
                return

            # Go to left subtree
            reverse_inorder(node.left)

        reverse_inorder(root)
        return self.ans