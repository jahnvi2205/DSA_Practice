def search(self, root, key):
        # code here
        # while root!= None:
        #     if root.data== key:
        #         return True
        #     elif root.data>key:
        #         root=root.left
        #     else:
        #         root=root.right
                
        # return False
            
            
        # recursive
        if root==None:
            return False
            
        elif root.data==key:
            return True
            
        elif root.data>key:
            return self.search(root.left,key)
            
        else :
            return self.search(root.right, key)