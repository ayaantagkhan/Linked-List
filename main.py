from linkelist import Node, LinkedList
from mergelinkedlist import mergeTwoLinkedLists
from reversal import Reversal

def testMerge():
    list1 = LinkedList()
    list2 = LinkedList()

    list1.push_back(1)
    list1.push_back(2)
    list1.push_back(3)


    list2.push_back(2)
    list2.push_back(3)
    list2.push_back(4)


    merged = mergeTwoLinkedLists(list1.head, list2.head)
    print("New Linked List head:", merged.data)

    while merged:
        print("Current Node: ", merged.data)
        merged = merged.next

def testReversal():

    list1 = LinkedList()
    list1.push_back(1)
    list1.push_back(2)
    list1.push_back(3)

    current = list1.head
    while current:
        print("Node Value:", current.data)
        current = current.next


def miscTestPrinter():

    ll = LinkedList()

    ll.push_back(10)
    ll.push_back(20)
    ll.push_back(30)
    
    current = ll.head
    while current:
        print("Value:", current.data)
        current = current.next

    print("Linked List Size:", ll.size())
    print("Is the Linked List Empty?:", ll.empty())
    print("Linked List value at Index 1 (starts at index 0):", ll.value_at(1))
    print("The head of the linked list is", ll.front())
    print("The back of the linked list is", ll.back())


testMerge()
# testReversal()
# miscTestPrinter()

