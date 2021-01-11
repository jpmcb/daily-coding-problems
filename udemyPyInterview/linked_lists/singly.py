class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

class Singly(object):

    def __init__(self):
        self.head = None

    def append_front(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        
    def print_list(self):
        current = self.head

        print('HEAD -> ', end='')
        while current != None:
            print(current.value, end='')
            print(' -> ', end='')
            current = current.next
        print('NONE')

ll = Singly()
ll.append_front(1)
ll.append_front(2)
ll.append_front(3)
ll.print_list()