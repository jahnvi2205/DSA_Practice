def isnumber(self,s):
        if s.startswith("-"):
            return s[1:].isdigit()
        return s.isdigit()
        
    def solve(self,a,b,op):
        if op== "+":
                return a+b
        elif op== "-":
                return a-b
        elif op== "*":
                return a*b
        elif op== "/":
                return a//b
        elif op== "^":
                return a**b
        else:
            return ValueError("Invalid Operation!")

    def evaluatePostfix(self, arr):
        stack=list()
        result= None
        for i in arr:
            if self.isnumber(i):
                stack.append(int(i))
            else:
                b= stack.pop()
                a= stack.pop()
                temp= self.solve(a,b, i)
                stack.append(temp)
                    
        return stack[0]