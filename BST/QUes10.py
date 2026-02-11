class Solution:
    def buildBST(self, arr, start, end):
        if start>end:
            return
        
        mid= (start+end)//2
        node= Node(arr[mid])
        
        node.left= self.buildBST(arr, start, mid-1)
        node.right= self.buildBST(arr, mid+1, end)
        return node
        
    def inorder(self,node,arr):
        if not node:
            return 
                
        self.inorder(node.left, arr)
        arr.append(node.data)
        self.inorder(node.right, arr)
    
        
    def balanceBST(self,root):
        arr=[]
        self.inorder(root,arr)
        return self.buildBST(arr, 0, len(arr)-1)