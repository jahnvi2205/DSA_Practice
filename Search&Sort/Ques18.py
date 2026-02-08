def minSwaps(self, arr):
		arr_pos= [(num,i) for i, num in enumerate(arr)]
		visited= [False]*len(arr)
		swap= 0
		arr_pos.sort()
		for i in range(0,len(arr)):
		    if visited[i] or arr_pos[i][1]==i:
		        continue
		    
		    cycle=0
		    j=i
		    
		    while not visited[j]:
		        visited[j]= True
		        j= arr_pos[j][1]
		        cycle+=1
		        
		    swap+= (cycle-1)
		return swap