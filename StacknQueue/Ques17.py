def getMaxArea(self, arr):
        # code here
        arr= arr+ [0]
        max_area= 0
        n= len(arr)
        s= []

        i= 0
        while i< n:
            if (not s) or (arr[i]> arr[s[-1]]):
                s.append(i)
                i+=1

            else:
                top= s.pop()
                height= arr[top]
                width= i if (not s) else (i-s[-1]-1)
                # print(height*width)
                max_area= max(max_area, height*width)

        return max_area