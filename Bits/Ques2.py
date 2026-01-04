class Solution:
	def singleNum(self, arr):
		xor_all=0
		for i in arr:
		    xor_all^= i
		    
		diff_bit = xor_all & -xor_all
		 
		a=0
		b=0
		 
		for num in arr:
		    if num & diff_bit:
		        a^= num
		         
		    else:
		        b^= num
		        
		return sorted([a,b])