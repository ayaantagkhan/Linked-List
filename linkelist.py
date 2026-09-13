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

    def pop_front(self):
        if self.head is None:
            return None

        value = self.head.data
        self.head = self.head.next

        return value

    def push_back(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def pop_back(self):
        # Check whether there is anything in the ll
        if self.head is None:
            return None

        # If there is only one item in the ll
        if self.head.next is None:
            value = self.head.data
            self.head = None
            return value

        # If we have to go through elements in the ll to reach the end and remove

        current = self.head

        while current.next.next:
            current = current.next

        value = current.next.data
        current.next = None

        return value

    def front(self):
        if self.head is None:
            return None

        return self.head.data

    def back(self):
        if self.head is None:
            return None

        current = self.head

        while current.next:
            current = current.next

        return current.data

    def insert(self, index, value):
        if index == 0:
            self.push_front(value)
            return value

        new_node = Node(value)
        current = self.head

        for i in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return value

    def erase(self, index):
        if self.head is None: 
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head

        for i in range(index - 1):
            current = current.next

        value = current.next.data
        current.next = current.next.next

        return value

    def value_n_from_end(self, n):
        first = self.head
        second = self.head

        for i in range(n):
            second = second.next

        while second:
            first = first.next
            second = second.next

        return first.data

    def reversal(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current 
            current = next_node

        self.head = previous

        
ll = LinkedList()

first = Node(10)
second = Node(20)
third = Node(30)


ll.head = first
first.next = second
second.next = third

# Removes the element at the head (first index) of the linked list 
# removed = ll.pop_front()
# print(removed, "was removed from the linked list.")

# Removes an element from the end of the LL
# print("Removed:", ll.pop_back())

# Adds a new element to the front of the LL
# print(ll.push_front(5))

# Adds a new element to the back of the LL
# ll.push_back(40)

# Inserts a new element at whichever index you choose (index, value of node)
# print("Inserted:", ll.insert(1,15))

# Erases an element from an index from the linked list
# print("Removed:", ll.erase(2))

# Get's the n'th value from the end 
# print(ll.value_n_from_end(2))

# Reverses the linked list 
# ll.reversal()

current = ll.head
while current:
    print("Value:", current.data)
    current = current.next

print("Linked List Size:", ll.size())
print("Is the Linked List Empty?:", ll.empty())
print("Linked List value at Index 1 (starts at index 0):", ll.value_at(1))
print("The head of the linked list is", ll.front())
print("The back of the linked list is", ll.back())




        