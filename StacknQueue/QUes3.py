class TwoStacks:
    def __init__(self):
        self.s1= []
        self.s2= []

    # Function to push an integer into stack 1
    def push1(self, x):
        self.s1.append(x)

    # Function to push an integer into stack 2
    def push2(self, x):
        self.s2.append(x)

    # Function to remove an element from top of stack 1
    def pop1(self):
        if not self.s1:
            return -1
            
        popped= self.s1.pop()
        return popped

    # Function to remove an element from top of stack 2
    def pop2(self):
        if not self.s2:
            return -1
            
        popped= self.s2.pop()
        return popped