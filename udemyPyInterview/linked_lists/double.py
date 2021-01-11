class Node(object):
    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

class Doubley(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, value):
        if self.head != None:
            new_node = Node(value, self.head, None)
            self.head.prev = new_node
            self.head = new_node

        else:
            new_node = Node(value, None, None)
            self.head = new_node
            self.tail = new_node
    
    def add_back(self, value):
        if self.tail != None:
            new_node = Node(value, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node

        else:
            new_node = Node(value, None, None)
            self.head = new_node
            self.tail = new_node

    def insert_after(self, node, value):
        new_node = Node(value)

        new_node.next = node.next
        new_node.prev = node

        node.next.prev = new_node

        node.next = new_node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = None
        node.prev = None

    def print_list(self):
        current = self.head

        print('HEAD <-> ', end='')
        while current != None:
            print(current.value, end='')
            print(' <-> ', end='')
            current = current.next
        print('TAIL')


ll = Doubley()
ll.add_front(4)
ll.add_front(3)
ll.add_front(2)
ll.add_front(1)
ll.add_back(5)
ll.add_back(6)
ll.add_back(7)
ll.insert_after(ll.head.next.next, 99)
ll.print_list()
ll.remove(ll.head.next.next.next)
ll.print_list()