class Stack(object):
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items==[]
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def allShow(self):
        return [x for x in self.items]

s=Stack()
print("is this list empty:",s.isEmpty())
for x in range(5):
    s.push(x**2)

print("all current elements of this stack s:",s.allShow())
print("the item removed is :",s.pop())
print("the top item on this stack:",s.peek())
print("current size of this list is:",s.size())
