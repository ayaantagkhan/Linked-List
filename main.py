from linkelist import Node, LinkedList

ll = LinkedList()

ll.push_back(10)
ll.push_back(20)
ll.push_back(30)


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