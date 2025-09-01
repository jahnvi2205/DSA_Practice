def threeWayPartition(self, arr, a, b):
	    s=0
	    e=len(arr)-1
	    i=0
	    while i<len(arr):
	        if e<i:
	            break
	        if arr[i]<a:
	            arr[i],arr[s]=arr[s],arr[i]
	            s+=1
	            i+=1
	        elif arr[i]>b:
	            arr[i],arr[e]=arr[e],arr[i]
	            e-=1
	           # i+=1
	        else:
	            i+=1