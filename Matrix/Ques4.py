def rowWithMax1s(self, arr):
        for i in range(0,len(arr[0])):
            for j in range(0,len(arr)):
                if arr[j][i]==1:
                    return j
        return -1