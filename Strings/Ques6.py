# Input: String first = "XY";
#     String second = "12";
#     String[] results = {"1XY2", "Y1X2", "Y21XX"};

# Output: 1XY2 is a valid shuffle of XY and 12
# Y1X2 is a valid shuffle of XY and 12     
# Y21XX is not a valid shuffle of XY and 12

def valid(s1,s2,result):
    if len(result) != (len(s1)+len(s2)):
        return False

    
    l1= list(s1)+ list(s2)
    return True if sorted(l1)== sorted(list(result)) else False

print(valid("ba","32","a33b"))