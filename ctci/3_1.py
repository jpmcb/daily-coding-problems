# Three in one


# --------------
# implementation: A fairly simple array that holds 3 stacks

class Multistack:
    def __init__(self, stacksize):
        self.numstacks = 3
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            raise Exception("Stack is full")
        self.sizes[stacknum] += 1
        self.array[self.index(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception("Stack is empty")
        value = self.array[self.index(stacknum)]
        self.array[self.index(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception("Stack is empty")
        return self.array[self.index(stacknum)]
    
    def isEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def isFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def index(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1
    

# -------
# Testing

newstack = Multistack(3)

print(newstack.isEmpty(0))
newstack.push(1, 0)
print(newstack.peek(0))
print(newstack.isEmpty(0))

print(newstack.isEmpty(1))
newstack.push(2, 1)
print(newstack.peek(1))
print(newstack.isEmpty(1))

print(newstack.isEmpty(2))
newstack.push(3, 2)
print(newstack.peek(2))
print(newstack.isEmpty(2))