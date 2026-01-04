# xor mein jo diff bit hoga vohi 1 hoga so count all that.. easy!!
class Solution:
    def countBitsFlip(self, a, b):
        #code here
        xor= a^b
        count=0
        
        while xor>0:
            count+= xor&1
            xor= xor>>1
        return count