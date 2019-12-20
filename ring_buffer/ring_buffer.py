from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == None and self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        elif self.storage.length < self.capacity:
            self.storage.add_to_head(item)
        else:
            self.current.value = item
            if self.current.prev != None:
                self.current = self.current.prev
            else:
                self.current = self.storage.tail


        
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.tail
        while node:
            list_buffer_contents.append(node.value)
            node = node.prev

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
