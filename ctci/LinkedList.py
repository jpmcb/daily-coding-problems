# Linked list implementation

from random import randint

class Node():
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class LinkedList():
    def __init__(self, values = None):
        self.head = None
        self.tail = None

        if values != None:
            for val in values:
                self.add(val)

    def __iter__(self):
        current = self.head
        while current != None:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count

    def add(self, value):
        if self.head == None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def generate(self, n, min_val, max_val):
        self.head = self.tail = None
        for _ in range(n):
            self.add(randint(min_val, max_val))
        return self

class DoublyLinkedList(LinkedList):
    def add(self, value):
        if self.head == None:
            self.tail = self.head = Node(value, None, None)
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
        return self