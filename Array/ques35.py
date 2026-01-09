def findMedian(self, arr):
        #code here.
        arr.sort()
        n=len(arr)
        if n % 2 == 1:
            return arr[n // 2]
        else:
            # Average of the two middle elements
            return (arr[(n // 2) - 1] + arr[n // 2]) / 2