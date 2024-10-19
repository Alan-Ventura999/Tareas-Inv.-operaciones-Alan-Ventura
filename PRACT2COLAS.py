class DLDqueue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, obj):
        new_node = self.Node(obj)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_last(self, obj):
        new_node = self.Node(obj)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove_first(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return data

    def remove_last(self):
        if not self.tail:
            return None
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return data

    def get_size(self):
        return self.size

class DQStack:
    def __init__(self):
        self.data = DLDqueue()

    def push(self, obj):
        self.data.insert_first(obj)

    def pop(self):
        return self.data.remove_first()

    def size(self):
        return self.data.get_size()


stack = DQStack()
stack.push(10)
stack.push(20)
print(f"Popped: {stack.pop()}")
print(f"Size: {stack.size()}")

class DQQueue:
    def __init__(self):
        self.data = DLDqueue()

    def enqueue(self, obj):
        self.data.insert_last(obj)

    def dequeue(self):
        return self.data.remove_first()

    def size(self):
        return self.data.get_size()


queue = DQQueue()
queue.enqueue(10)
queue.enqueue(20)
print(f"Dequeued: {queue.dequeue()}")
print(f"Size: {queue.size()}") 