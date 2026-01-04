from collections import deque
class Solution:
	def firstNonRepeating(self, s):
		q= deque()
		freq= [0]*26
		result= ""
		for ch in s:
		    idx= ord(ch)- ord('a')
		    freq[idx]+= 1
		        
		    q.append(ch)
		    while q and freq[ord(q[0])- ord('a')]>1:
		        q.popleft()      # using this function for O(1)
		        
		    if q:
		        result += q[0]
		    else:
		        result+= "#"
		        
		return result
		
# “Deque allows O(1) insertion and deletion from both ends,
# whereas list operations at the front are O(n).”
# Queue logic? → deque
# Indexing? → list