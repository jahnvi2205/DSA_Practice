        arr.sort()
        l = len(arr)
        
        for i in range(l-2):
            left, right = i+1, l-1
            while left < right:
                s = arr[i]+arr[left]+arr[right]
                if s==target:
                    return True
                elif s<target:
                    left +=1
                else:
                    right -=1
        return False
