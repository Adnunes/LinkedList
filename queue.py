from linked_list import Node

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size  = 0

    def peek(self):
        if self.is_empty():
            print('Nothing to see here!')
        else:
            return  self.head.get_value()
        
    def get_size(self):
        return self.size
    
    def has_space(self):
        if self.max_size == None:
            return True
        elif self.max_size > self.size:
            return True
        else:
            return False

    def is_empty(self):
        return self.size ==0
    
    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print(f'Adding {item_to_add.get_value()} to the queue!')
            
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add

            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add

            self.size +=1
        else:
            print('Sorry, no more room!')

    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            print(f'{item_to_remove.get_value()} is served!')
            
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            
            self.size -= 1

        else:
            print('this queue is totally empty!')

        
print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue(10)
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
# ------------------------ #

deli_line.enqueue("western omelet with home fries")
# ------------------------ #

print(f"------------\nOur first order will be {deli_line.peek()}")
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
# ------------------------ #

deli_line.dequeue()
# ------------------------ #