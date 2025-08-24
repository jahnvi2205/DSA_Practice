def count_smaller_equal(self,row, x):
        """Return count of elements <= x in sorted row (manual binary search)."""
        l, r = 0, len(row)
        while l < r:
            mid = (l + r) // 2
            if row[mid] <= x:
                l = mid + 1
            else:
                r = mid
        return l  # number of elements <= x

    def median(self,mat):
        n = len(mat)
        m = len(mat[0])
    
    # low = min element in first column
        low = min(row[0] for row in mat)
    # high = max element in last column
        high = max(row[-1] for row in mat)
    
        desired = (n * m + 1) // 2
    
        while low < high:
            mid = (low + high) // 2
        
        # Count how many numbers <= mid
            count = 0
            for row in mat:
                count += self.count_smaller_equal(row, mid)
        
            if count < desired:
                low = mid + 1
            else:
                high = mid
    
        return low

