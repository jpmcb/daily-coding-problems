from stack import Stack

class Queue(object):
    def __init__(self):
        self.current = Stack()
        self.backup = Stack()

    def enqueue(self, item):
        self.current.push(item)

    def dequeue(self):
        while not self.current.isEmpty():
            element = self.current.pop()
            self.backup.push(element)

        target = self.backup.pop()

        while not self.backup.isEmpty():
            element = self.backup.pop()
            self.current.push(element)

        return target

    def isEmpty(self):
        return self.current.isEmpty()

    def size(self):
        return self.current.size()

    def get_queue(self):
        print('current: ', self.current.get_stack())
        print('backup: ', self.backup.get_stack())

q = Queue()
print(q.size())
print(q.isEmpty())
q.enqueue(1)
print(q.size())
print(q.isEmpty())
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.get_queue()
print(q.dequeue())
q.get_queue()
print(q.dequeue())
q.get_queue()
print(q.dequeue())
q.get_queue()
print(q.dequeue())
q.get_queue()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print(q.dequeue())