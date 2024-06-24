class MyQueue:


    def __init__(self):
        # only pushing takes place here
        self.s1 = []

        # only popping takes place here
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if self.s2:
            return self.s2.pop()
        
        # if stack 2 is empty move all elements from stack 1 to stack 2 
        # then remove the last element of stack 2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop()
    
    def peek(self) -> int:
        
        if self.s2:
            return self.s2[-1]
        # similarly, if stack two doesnt exist, pop from s1 and push to s2 till s1 is empty
        # then remove stack[top]
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2[-1]
        # return self.s2[-1]
        

    def empty(self) -> bool:
        if not self.s1 and not self.s2:
            return True
        return False