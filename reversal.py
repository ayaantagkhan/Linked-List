from linkelist import Node, LinkedList

# Reverse a Linked List Problem

def Reversal(LinkedList):
    previous = None
    current = LinkedList.head

    while current:
        next_node = current.next
        current.next = previous
        previous = current 
        current = next_node 

        LinkedList.head = previous 

            