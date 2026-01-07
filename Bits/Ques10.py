def AllPossibleStrings(self, s):
		ans= []
		n= len(s)
		for mask in range(1, 1<<n):
		    subseq=""
		    for i in range(n):
		        if mask & (1<<i):
		            subseq+= s[i]
		    ans.append(subseq)
		
		ans.sort()
		return ans