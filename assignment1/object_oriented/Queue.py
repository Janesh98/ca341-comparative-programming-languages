class Queue:

    def __init__(self):
        self.queue = []

    def put(self, item):
        self.queue.append(item)

    def get(self):
        return self.queue.pop(0)

    def empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)