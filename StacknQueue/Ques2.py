class Queue:
    def __init__(self,n):
        self.cap= n
        self.cont= [None]* n
        self.front=-1
        self.rear=-1

    def is_empty(self):
        return self.rear== -1 

    def is_full(self):
        return self.rear== (self.cap-1)

    def get_front(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        
        return self.cont[self.front]

    def get_rear(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        
        return self.cont[self.rear]

    def Enqueue(self,num):
        if self.is_full():
            print("Queue is full!")
            return

        elif self.is_empty():
            self.front=0
            self.rear=0
        else:
            self.rear+=1
            
        self.cont[self.rear]=num
        return True


    def Deque(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        popped= self.cont[self.front]
        
        if self.front == self.rear:
            self.front= -1
            self.rear= -1
        else:
            self.front+=1

        return popped