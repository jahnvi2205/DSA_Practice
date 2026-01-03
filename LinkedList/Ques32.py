def multiply_two_lists(self, first, second):
        # Code here
        Mod= 10**9+7
        
        num1= 0
        dummy1= first
        while dummy1:
            num1= (num1*10+ dummy1.data)% Mod
            dummy1= dummy1.next
          
        num2= 0  
        dummy2= second
        while dummy2:
            num2= ((num2*10)+ dummy2.data)%Mod
            dummy2= dummy2.next
            
            
        result= (num1* num2)% Mod
        return result