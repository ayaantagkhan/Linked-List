class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None #First Node

    def size(self):
        count = 0
        current = self.head

        while current:
            count+=1
            current = current.next

        return count

    def empty(self):
        return self.head is None

    def value_at(self, index):
        count = 0
        current = self.head

        while current:
            if count == index:
                return current.data

            count+=1
            current = current.next

        return None

    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node



ll = LinkedList()

first = Node(10)
second = Node(20)
third = Node(30)


ll.head = first
first.next = second
second.next = third

print(ll.push_front(5))

current = ll.head


while current:
    print(current.data)
    current = current.next

print(ll.size())
print(ll.empty())
print(ll.value_at(0))



        