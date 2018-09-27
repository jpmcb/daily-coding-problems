# Stack min

class MinStack:
    minStack = []
    numStack = []

    def push(self, element):
        if len(self.minStack) == 0:
            self.minStack.append(element)
        elif self.minStack[-1] >= element:
            self.minStack.append(element)
        self.numStack.append(element)

    def pop(self):
        if self.isEmpty(): 
            raise Exception("Stack is empty")
        value = self.numStack.pop()
        if value == self.minStack[-1]:
            self.minStack.pop()
        return value

    def peek(self):
        return self.numStack[-1]

    def isEmpty(self):
        return len(self.numStack) == 0

    def min(self):
        return self.minStack[-1]

stack = MinStack()
stack.push(3)
stack.push(1)
stack.push(4)
stack.push(5)

print(stack.min())
print(stack.pop())
print(stack.peek())
print(stack.min())

stack.push(-1)
stack.push(9)
stack.push(8)

print(stack.min())
print(stack.pop())
print(stack.peek())
print(stack.min())