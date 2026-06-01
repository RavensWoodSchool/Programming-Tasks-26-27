"""
TASK: 03 Queue Simulation

# Queue Simulation using OOP
Make a Queue class with:
- enqueue, dequeue, peek, size  
Simulate customers joining/leaving.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

class Queue:
    def__init__(self):
    self.items = []

def enqueue(self, item):
    self.items.append(item)

def dequeue(self):
    if self.is_empty():
        return self.items.pop(0)
    return self.items.pop(0)

def peek(self):
    if self.is_empty():
        return"Queue is empty"
    return self.items[0]
