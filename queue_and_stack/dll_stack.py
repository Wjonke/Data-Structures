import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
            # Because a DLL can very efficiently add and remove things without shifting.
            # its worse at access but we dont really need to access anything specifically or sort it
            # Stack is going to use LIFO vs FIFO of queue, last in first out
            # much like stacking cards and drawing from a deck
            #top of deck is on top, add to top, remove from top(head)

        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value): #add to the start of the DLL (head)
        self.storage.add_to_head(value)

    def pop(self): #delete from the start of the DLL (head)
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.length
