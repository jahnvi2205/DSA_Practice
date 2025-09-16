class Stack:
    def __init__(self,n):
        self.cap= n
        self.cont= [None]*n
        self.top= -1

    def is_empty(self):
        return self.top==-1

    def is_full(self):
        return self.top== (self.cap-1)

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.cont[self.top]

    def push(self, num):
        if  self.is_full():
            print("Stack is full")
            return False

        self.top+= 1
        self.cont[self.top]= num
        return True

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        popped= self.cont[self.top]
        self.top -=1
        return popped


        

        
        
        




