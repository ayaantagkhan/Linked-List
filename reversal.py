class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Reversal(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current 
            current = next_node 

        self.head = previous 

            