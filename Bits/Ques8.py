'''1 left shift   → ×2
2 left shifts  → ×4
3 left shifts  → ×8 '''

def divide(self, dividend, divisor):
        negative= (dividend<0)!= (divisor<0)
          
        divisor= abs(divisor)
        dividend= abs(dividend)
        
        quotient= 0
        
        while dividend>= divisor:
            temp= divisor
            multiple= 1
            while dividend>= (temp<<1):
                temp= temp<<1
                multiple= multiple<<1
        
            dividend = dividend-temp
            quotient+=multiple
            
        if quotient > 2**31 -1:
            return 2**31 -1
        elif quotient < -2**31:
            return -2**31
        
        return -quotient if negative else quotient