from linkelist import Node, LinkedList

# Merge Linked List and return the value of the head of the list problem


def mergeTwoLinkedLists(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 and list2:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2
                
    return dummy.next

# while current:
    # print("List 1 Node Value: ", current.data)
    # current = current.next 

# while current2:
    # print("List 2 Node Value: ", current2.data)
    # current2 = current2.next