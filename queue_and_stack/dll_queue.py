import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList() #setting storage used to an empty DLL instance
        #storage now references DLL file
        # we can call the methods we created there inside here

        # Why is our DLL a good choice to store our elements?
            # Because a DLL can very efficiently add and remove things without shifting.
            #its worse at access but we dont really need to access anything specifically or sort it
            # Tail is the back of the queue and head is the front of the line

    def enqueue(self, value): #insert, add to back of queue
        self.storage.add_to_tail(value)

    def dequeue(self): #delete
        #grab what is being deleted, set it to a variable and return it, that way we have access to it's value after delete
        self.size -= 1
        return self.storage.remove_from_head()

    def len(self): #track length of queue
        return self.storage.length
