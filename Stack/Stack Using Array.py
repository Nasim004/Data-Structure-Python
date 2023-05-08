class stackArray:
    def __init__(self):
        self.stack= [None]* 5
        self.top=-1
    def push(self,data):     
            self.top=self.top+1
            self.stack[self.top]=data
    
    def pop(self):
        self.stack[self.top]=0
        self.top=self.top-1

           
        
    def display(self):
        if self.top ==-1:
            print("stack underflow")
            return
        temp=self.top
        i=0
        while i <=temp:
            print(self.stack[i])
            i=i+1

        
stack=stackArray()
stack.push(10)
stack.push(20)
stack.push(50)
stack.push(40)
stack.push(300)
stack.display()
print("popped once")
stack.pop()
stack.display()
print("popped all elemnts and then also trying to pop:")
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.display()