from linkelist import Node, LinkedList

def Reversal(self):
    previous = None
    current = self.head

    while current:
        next_node = current.next
        current.next = previous
        previous = current 
        current = next_node 

        self.head = previous 

            